# ----------------------------------------------------------
# conditional_statements.py
# MODULE: Conditional Statements (IF–ELIF–ELSE Chain)
# ----------------------------------------------------------
# CONTENTS:
#   1. What are Conditional Statements?
#   2. Why do we need ELIF?
#   3. Syntax of IF–ELIF–ELSE
#   4. Multiple-branch decision patterns
#   5. Nested conditional statements
#   6. Match-case (Python 3.10+) alternative
#   7. Common errors & pitfalls
#   8. Real-world examples
#   9. DSA-style problems (with solutions)
#  10. Mini assert-based test suite
# ----------------------------------------------------------


# ----------------------------------------------------------
# 1) WHAT ARE CONDITIONAL STATEMENTS?
# ----------------------------------------------------------
# Conditional statements allow a program to make MULTIPLE decisions.
# They evaluate conditions in a top-down manner.
#
# The structure is:
#   if CONDITION:
#       block
#   elif CONDITION:
#       block
#   elif CONDITION:
#       block
#   else:
#       fallback block
#
# Python executes ONLY the first TRUE condition and SKIPS the rest.


# ----------------------------------------------------------
# 2) WHY DO WE NEED ELIF?
# ----------------------------------------------------------
# ELIF lets us handle multiple mutually-exclusive choices.
# Instead of:
#   if ...
#   if ...
#   if ...
#
# ELIF ensures:
#  - Cleaner decision tree
#  - Only ONE branch runs
#  - More readable and efficient


# ----------------------------------------------------------
# 3) BASIC SYNTAX (must learn!)
# ----------------------------------------------------------
value = 75

if value >= 90:
    print("Grade: A")
elif value >= 80:
    print("Grade: B")
elif value >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Notes:
#  - Every line ends with a colon :
#  - Indentation defines code blocks (normally 4 spaces)
#  - Only ONE block executes (first true condition)


# ----------------------------------------------------------
# 4) MULTIPLE-BRANCH DECISIONS (CHAIN)
# ----------------------------------------------------------
# Example: Categorizing Age
age = 19

if age < 0:
    print("Invalid age")
elif age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")

# This shows how a chain of elif can create a decision ladder.


# ----------------------------------------------------------
# 5) NESTED CONDITIONAL STATEMENTS
# ----------------------------------------------------------
# You can put one IF inside another.
income = 70000
credit_score = 720

if income > 50000:
    if credit_score >= 700:
        print("Loan Approved")
    else:
        print("Loan Denied: Low Credit Score")
else:
    print("Loan Denied: Low Income")


# ----------------------------------------------------------
# 6) match-case (Python 3.10+)
# ----------------------------------------------------------
# A cleaner alternative to long elif chains.
# Works like switch-case in other languages.
#
# Example:
user_role = "admin"

match user_role:
    case "admin":
        print("Full Access")
    case "editor":
        print("Edit Access")
    case "viewer":
        print("Read-Only Access")
    case _:
        print("Unknown role")


# ----------------------------------------------------------
# 7) COMMON ERRORS WITH CONDITIONAL STATEMENTS
# ----------------------------------------------------------
# ❌ ERROR 1 — Using '=' instead of '==' 
# if x = 10:   # WRONG → '=' is assignment
# if x == 10:  # CORRECT

# ❌ ERROR 2 — Bad indentation
# if x > 5:
# print("Hi")   # WRONG (not indented)
#
# ❌ ERROR 3 — Writing unnecessary repeated IFs instead of ELIF
# if x > 10:
# ...
# if x > 5:
# ...
# This checks both conditions, not ideal. Use ELIF.

# ❌ ERROR 4 — Forgetting the else default case.
# else helps catch unexpected inputs and prevent bugs.


# ----------------------------------------------------------
# 8) REAL-WORLD EXAMPLES
# ----------------------------------------------------------

# Example 1: Password strength
pwd = "hello123"

if len(pwd) >= 12:
    print("Strong Password")
elif len(pwd) >= 8:
    print("Medium Password")
else:
    print("Weak Password")


# Example 2: Deciding fare based on passenger type
passenger = "student"

if passenger == "senior":
    discount = 50
elif passenger == "student":
    discount = 30
elif passenger == "child":
    discount = 70
else:
    discount = 0

print("Discount:", discount, "%")


# Example 3: Menu options
option = 3

if option == 1:
    print("Start")
elif option == 2:
    print("Settings")
elif option == 3:
    print("Exit")
else:
    print("Invalid option")


# ----------------------------------------------------------
# 9) DSA-STYLE CONDITIONAL PROBLEMS
# ----------------------------------------------------------

# PROBLEM 1:
# Find largest of 3 numbers.
# Complexity: O(1)
def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c


# PROBLEM 2:
# Classify a number as:
#   - Positive
#   - Negative
#   - Zero
def classify_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"


# PROBLEM 3:
# Determine traffic light action.
# Complexity: O(1)
def traffic_action(light):
    if light == "red":
        return "STOP"
    elif light == "yellow":
        return "READY"
    elif light == "green":
        return "GO"
    else:
        return "INVALID"


# PROBLEM 4:
# Check if character is vowel or consonant.
def check_char(ch):
    vowels = "aeiouAEIOU"
    if ch in vowels:
        return "vowel"
    elif ch.isalpha():
        return "consonant"
    else:
        return "not a letter"


# PROBLEM 5:
# Movie ticket pricing:
# - Child < 12: ₹100
# - Adult 12–59: ₹200
# - Senior ≥60: ₹150
def ticket_price(age):
    if age < 12:
        return 100
    elif age < 60:
        return 200
    else:
        return 150


# ----------------------------------------------------------
# 10) MINI TEST SUITE (assertions)
# ----------------------------------------------------------
if __name__ == "__main__":
    print("\nRunning Conditional Statements Tests...\n")

    # Test largest_of_three
    assert largest_of_three(10, 5, 2) == 10
    assert largest_of_three(1, 9, 3) == 9

    # Test classify_number
    assert classify_number(10) == "Positive"
    assert classify_number(-3) == "Negative"
    assert classify_number(0) == "Zero"

    # Test traffic_action
    assert traffic_action("green") == "GO"
    assert traffic_action("red") == "STOP"
    assert traffic_action("yellow") == "READY"

    # Test check_char
    assert check_char("a") == "vowel"
    assert check_char("B") == "consonant"
    assert check_char("1") == "not a letter"

    # Test ticket_price
    assert ticket_price(10) == 100
    assert ticket_price(25) == 200
    assert ticket_price(70) == 150

    print("All tests passed ✔️")
    print("\nEnd of file.\n")

# ----------------------------------------------------------
# END OF FILE
# ----------------------------------------------------------
