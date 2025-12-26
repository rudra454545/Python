# variables_and_expressions.py
# -----------------------------------------
# Module: Variables & Expressions 
# Author: Rudra Prasad Dutta
# Purpose: Teach variables, expressions, syntax, examples, storing into a DB,
#          and common DSA-style questions + answers — all explanations are comments.
# -----------------------------------------

# -----------------------------
# 1) What is a variable? (Definition)
# -----------------------------
# A variable is a name that refers to a value in memory.
# In Python, you create a variable by assignment using '='.
# Python is dynamically typed: you don't declare types explicitly.
#
# Examples of variables and types:
x = 10                 # integer
pi = 3.14159           # float (real number)
name = "Rudra"         # string (sequence of characters)
is_ready = True        # boolean (True/False)
numbers = [1, 2, 3]    # list (ordered, mutable sequence)
person = {"age": 21, "city": "Rourkela"}  # dict (mapping)

# -----------------------------
# 2) Basic expressions & operators
# -----------------------------
# An expression combines values, variables and operators and produces a value.
# Common operators:
#   Arithmetic: +, -, *, /, // (floor division), % (mod), ** (power)
#   Comparison: ==, !=, >, <, >=, <=  (these return booleans)
#   Logical: and, or, not
#   Membership: in, not in
#   Identity: is, is not
#
# Examples:
a = 5
b = 2
add = a + b          # 7
sub = a - b          # 3
mul = a * b          # 10
div = a / b          # 2.5  (true division, result is float)
floordiv = a // b    # 2    (integer division)
mod = a % b          # 1
power = a ** b       # 25   (5^2)

# precedence example:
expr = 3 + 4 * 2      # multiplication first -> 3 + (4*2) = 11

# parentheses override precedence:
expr2 = (3 + 4) * 2   # = 14

# string concatenation and repetition:
greeting = "Hello, " + name
laugh = "ha" * 3      # "hahaha"

# boolean expressions:
is_big = a > 100      # False
cond = (a > 0) and (b > 0)  # True

# -----------------------------
# 3) Assignment variations & shorthand
# -----------------------------
# You can update variables with shorthand operators:
n = 10
n += 5   # n = n + 5  -> 15
n *= 2   # n = n * 2  -> 30

# multiple assignment:
x, y, z = 1, 2, 3
# swap variables neatly:
x, y = y, x

# -----------------------------
# 4) Type casting / conversion
# -----------------------------
# Convert types explicitly with int(), float(), str(), bool(), list(), dict(), tuple()
num_str = "123"
num = int(num_str)    # 123
f = float("3.14")     # 3.14
s = str(100)          # "100"

# Safe conversion: catch ValueError
try:
    bad = int("hello")
except ValueError:
    bad = None  # fallback

# -----------------------------
# 5) Variable naming rules & best practices
# -----------------------------
# - Start with a letter or underscore, followed by letters, digits, or underscores.
# - Case-sensitive: 'data' != 'Data'
# - Use meaningful names: student_count, average_score
# - Constants by convention: UPPER_CASE names (Python doesn't enforce immutability)

# -----------------------------
# 6) Mutability vs Immutability
# -----------------------------
# Immutable types: int, float, str, tuple, frozenset
# Mutable types: list, dict, set, bytearray
#
# Example:
t = (1, 2, 3)  # tuple -> cannot change elements
lst = [1, 2, 3]
lst[0] = 100   # allowed because list is mutable

# -----------------------------
# 7) Scope (local vs global)
# -----------------------------
global_var = "I am global"

def func():
    # local_var is local to func
    local_var = "I am local"
    # to modify a global variable inside function:
    # global global_var
    # global_var = "changed"
    return local_var

# -----------------------------
# 8) Expressions used in real code (examples)
# -----------------------------
# compute area of circle using variables and expressions
radius = 2.5
area = pi * (radius ** 2)

# format strings (f-strings)
message = f"Hello {name}, radius {radius} => area {area:.2f}"

# -----------------------------
# 9) Storing variables/expressions into a database (SQLite example)
# -----------------------------
# We'll demonstrate: create a table, insert values (variables), query them back.
#
# SQLite is chosen because it's built-in (no external packages). This pattern applies
# to other DBs (MySQL/Postgres) with appropriate drivers and connection strings.
#
# Steps:
#  1) import sqlite3
#  2) connect to a database file (or :memory: for ephemeral DB)
#  3) create table
#  4) insert using parameterized queries to prevent injection
#  5) query rows back and use variables to reconstruct Python values
#
# Example code (runnable):
import sqlite3
import json  # for storing complex objects as JSON strings (optional)

def db_demo():
    # Connect to a SQLite database file (it will be created if not exists)
    conn = sqlite3.connect("variables_demo.db")
    cur = conn.cursor()

    # Create a simple table to store variable snapshots
    cur.execute("""
    CREATE TABLE IF NOT EXISTS snapshots (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        value_text TEXT,
        value_type TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Example variables to store
    username = name                 # string variable
    score = 95                      # int variable
    meta = {"lang": "python", "level": "beginner"}  # dict -> needs serialization

    # When storing, convert to text safely. We store the type to interpret on read.
    cur.execute("INSERT INTO snapshots (name, value_text, value_type) VALUES (?, ?, ?)",
                ("username", username, "str"))
    cur.execute("INSERT INTO snapshots (name, value_text, value_type) VALUES (?, ?, ?)",
                ("score", str(score), "int"))
    # store JSON for complex objects
    cur.execute("INSERT INTO snapshots (name, value_text, value_type) VALUES (?, ?, ?)",
                ("meta", json.dumps(meta), "json"))

    conn.commit()

    # Query back
    cur.execute("SELECT id, name, value_text, value_type, created_at FROM snapshots")
    rows = cur.fetchall()
    print("\n--- DB Snapshots ---")
    for row in rows:
        rid, rname, rvalue_text, rtype, created_at = row
        # interpret based on rtype
        if rtype == "int":
            rvalue = int(rvalue_text)
        elif rtype == "float":
            rvalue = float(rvalue_text)
        elif rtype == "json":
            rvalue = json.loads(rvalue_text)
        else:
            rvalue = rvalue_text  # str or fallback

        print(f"{rid}: {rname} ({rtype}) = {rvalue}   inserted_at: {created_at}")

    # Clean up
    conn.close()

# Run the DB demo if file executed directly
if __name__ == "__main__":
    print("=== Variables & Expressions Demo ===")
    print("Examples of variable values:")
    print(f"x={x}, pi={pi}, name='{name}', is_ready={is_ready}")
    print("Sample expressions:")
    print(f"{a} + {b} = {add}, {a} ** {b} = {power}")
    print(message)
    db_demo()

# -----------------------------
# 10) Common DSA-style questions on variables & expressions (and answers)
# -----------------------------
# Q1: Given a list of numbers stored in a variable, write code to compute the sum, max, min.
# A1: Use built-in functions sum(), max(), min(). Complexity: O(n) time, O(1) extra space.
#
# Example (answer):
# nums = [3, 1, 4, 1, 5]
# total = sum(nums)
# maximum = max(nums)
# minimum = min(nums)
#
# Q2: If given a huge list of numbers streamed one by one, how to compute running average without storing all numbers?
# A2: Maintain two variables: running_sum and count. For each new number x:
#    running_sum += x
#    count += 1
#    running_avg = running_sum / count
# Complexity: O(1) per update, memory O(1).
#
# Q3: Sorting-related question: If variables hold small arrays, what is complexity of sorting using Python's sorted()?
# A3: Python's Timsort takes O(n log n) worst-case time and O(n) worst-case extra space. For nearly-sorted data it performs better.
#
# Q4: Given a string variable, reverse it. What's the simplest approach? Complexity?
# A4: Use slicing: reversed_s = s[::-1]; Complexity O(n) time and O(n) extra space for new string.
#
# Q5: Describe difference between copying a list by assignment vs copy() vs list().
# A5:
#    - new = old  -> both names reference same list (shallow alias); changes reflect in both.
#    - new = old.copy() or list(old) -> shallow copy; new list with same elements; nested mutable elements still shared.
#    - For deep copy of nested structures use copy.deepcopy().
#
# Q6: How to store a Python dictionary variable into a relational DB field?
# A6: Serialize (e.g., JSON) and store as TEXT (or use JSON column type if DB supports). When retrieving, parse JSON back into a dict.
#
# Q7: Complexity question on variable lookup: What's the time cost to access a local variable vs global vs builtins?
# A7: Local variable access is fastest (CPython optimizes locals), global access requires dictionary lookup in globals(), builtins requires another lookup. All are typically O(1) average-case but locals are fastest due to bytecode optimizations.
#
# Q8: Given two variables a and b, swap them without using a temporary variable. How?
# A8: Pythonic way: a, b = b, a
#    Alternatively (numeric): a = a + b; b = a - b; a = a - b  (but beware overflow/precision issues)
#
# Q9: Given a variable that might be None or an integer, what's the safe way to add 5?
# A9: Use conditional handling:
#    if x is None:
#        result = None  # or some default
#    else:
#        result = x + 5
# Or using a default: result = (x or 0) + 5  # note: this treats 0 as falsy too
#
# Q10: Interview-style puzzle:
#    Given a list 'nums', find whether any two numbers sum to target T.
# Approach:
#    Use a hash set storing seen numbers; for each x in nums check if (T - x) in set.
# Complexity: O(n) time, O(n) space.
#
# Example code (answer):
# def two_sum_exists(nums, T):
#     seen = set()
#     for x in nums:
#         if T - x in seen:
#             return True
#         seen.add(x)
#     return False
#
# -----------------------------
# 11) Summary / Study Tips (short, academic + conversational)
# -----------------------------
# - Master the basic types and how to convert between them. Practice small expressions.
# - Understand mutability: know which operations change objects vs reassign names.
# - Learn to reason about time/space when using variables in algorithms (e.g., scanning lists -> O(n)).
# - Practice storing Python values in databases: remember to serialize complex objects safely.
# - In interviews, explain the variable storage and how your code updates variables step-by-step.


#Local Vs Global Variables
# ------------------------------------------------------------
# LOCAL vs GLOBAL VARIABLES IN PYTHON — COMPLETE NOTES
# ------------------------------------------------------------

# ------------------------------------------------------------
# 1. DEFINITION
# ------------------------------------------------------------
# Local Variable:
#   - A variable declared inside a function.
#   - Exists ONLY inside that function.
#
# Global Variable:
#   - A variable declared outside all functions.
#   - Accessible throughout the entire module.


# ------------------------------------------------------------
# 2. SCOPE (WHERE IT CAN BE USED)
# ------------------------------------------------------------
# Local:
#   - Scope is limited to the function it is defined in.
#   - Cannot be accessed outside its function.
#
# Global:
#   - Scope is the whole program.
#   - Can be read from inside any function.


# ------------------------------------------------------------
# 3. LIFETIME (WHEN IT EXISTS)
# ------------------------------------------------------------
# Local:
#   - Created when the function starts.
#   - Destroyed when the function ends.
#
# Global:
#   - Created when the program starts running.
#   - Destroyed when the program ends.


# ------------------------------------------------------------
# 4. MODIFICATION RULE
# ------------------------------------------------------------
# Local:
#   - Free to modify inside the function.
#
# Global:
#   - Cannot be reassigned inside a function
#     unless the keyword "global" is used.
#
# Example:
#   global x
#   x = x + 1


# ------------------------------------------------------------
# 5. MEMORY LOCATION (NAMESPACE)
# ------------------------------------------------------------
# Local:
#   - Stored in the function’s local namespace (stack frame).
#
# Global:
#   - Stored in the module’s global namespace (dictionary-like).


# ------------------------------------------------------------
# 6. PERFORMANCE
# ------------------------------------------------------------
# Local:
#   - Faster access (lookups are optimized inside functions).
#
# Global:
#   - Slightly slower (Python checks locals → enclosing → global → builtins).


# ------------------------------------------------------------
# 7. RISK FACTOR
# ------------------------------------------------------------
# Local:
#   - Safer → no accidental modification of other parts of program.
#
# Global:
#   - Risky → overuse can cause bugs, harder to track state changes.


# ------------------------------------------------------------
# 8. READABILITY & CLEAN CODE
# ------------------------------------------------------------
# Local:
#   - Preferred. Keeps functions independent and testable.
#
# Global:
#   - Should be minimized. Use only for constants or shared configuration.


# ------------------------------------------------------------
# 9. MUTABILITY DIFFERENCE
# ------------------------------------------------------------
# Local:
#   - Affects only the function.
#
# Global:
#   - If global variable is MUTABLE (list, dict), you can MODIFY contents
#     WITHOUT using the 'global' keyword.
#
# Example:
#   my_list.append(10)  # allowed without global
#
# BUT to reassign it:
#   global my_list
#   my_list = [1,2,3]


# ------------------------------------------------------------
# 10. LEGB RULE (LOOKUP ORDER)
# ------------------------------------------------------------
# Python resolves variable names in:
#
#   L → Local
#   E → Enclosing (outer function)
#   G → Global
#   B → Builtins
#
# Local variables always have first priority.


# ------------------------------------------------------------
# 11. TABLE SUMMARY
# ------------------------------------------------------------
# | FEATURE           | LOCAL VARIABLE                 | GLOBAL VARIABLE               |
# |------------------|-------------------------------|------------------------------|
# | Declared in      | Inside a function             | Outside all functions        |
# | Scope            | Only that function            | Entire file/program          |
# | Lifetime         | During function execution     | Entire program execution     |
# | Modify inside fn | Allowed                       | Needs 'global' keyword       |
# | Speed            | Faster access                 | Slightly slower              |
# | Risk             | Low risk                      | Higher risk (shared state)   |
# | Best use         | Temporary values              | Constants/shared config      |


# ------------------------------------------------------------
# 12. CODE EXAMPLES
# ------------------------------------------------------------

x = 10  # global variable

def demo_local():
    # This x is LOCAL — it does NOT change the global x
    x = 5
    print("Inside demo_local, local x =", x)

def demo_global():
    global x  # tells Python to use the global x
    x = 50    # modifies the global variable
    print("Inside demo_global, modified global x =", x)

def demo_mutable_global():
    # Demonstrates mutable global without 'global'
    global_list.append("added")  # append allowed
    print("Inside demo_mutable_global, global_list =", global_list)


# Mutable global example:
global_list = []

# ------------------------------------------------------------
# Run the examples
# ------------------------------------------------------------

print("Global x initially =", x)
demo_local()
print("Global x after demo_local =", x)   # still 10

demo_global()
print("Global x after demo_global =", x)  # now 50

demo_mutable_global()
print("Final global_list =", global_list)

# ------------------------------------------------------------
# END OF FILE
# ------------------------------------------------------------