# ----------------------------------------------------------
# conditional_code.py
# MODULE: Conditional Code (IF / ELIF / ELSE)
# ----------------------------------------------------------
# This file contains:
#   1. What is Conditional Code?
#   2. Syntax of IF, ELIF, ELSE
#   3. Comparison operators used in conditions
#   4. Nested conditionals
#   5. Common mistakes beginners make
#   6. Real-world examples
#   7. DSA-style conditional problems + answers
#   8. Mini test cases (assert)
# ----------------------------------------------------------


# ----------------------------------------------------------
# 1) What is CONDITIONAL CODE?
# ----------------------------------------------------------
# Conditional code allows a program to make decisions.
# Based on conditions (True/False expressions), Python chooses
# which block of code to execute.
#
# The basic decision keyword is:  if
# Extra branches:  elif  (else-if)
# Final fallback:  else
#
# Conditionals help programs behave differently depending on input/data.


# ----------------------------------------------------------
# 2) BASIC SYNTAX
# ----------------------------------------------------------
# if condition:
#     # code runs if condition is True
# elif another_condition:
#     # runs if above 'if' was False and this is True
# else:
#     # runs if all above conditions were False
#
# IMPORTANT:
#   - USE COLON ':' at the end of each condition line.
#   - INDENT the code block under each condition (4 spaces).
#
# Example:
x = 10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")


# ----------------------------------------------------------
# 3) COMPARISON & LOGICAL OPERATORS
# ----------------------------------------------------------
# Conditions use comparison and logical operators.
#
# Comparison operators:
#   ==   equals
#   !=   not equal
#   >    greater than
#   <    less than
#   >=   greater or equal
#   <=   less or equal
#
# Logical operators:
#   and  -> both conditions must be True
#   or   -> at least one must be True
#   not  -> inverts True/False
#
# Example:
age = 20

if age >= 18 and age < 60:
    print("Adult (working age)")
elif age >= 60:
    print("Senior citizen")
else:
    print("Minor")


# ----------------------------------------------------------
# 4) NESTED CONDITIONALS
# ----------------------------------------------------------
# You can have an IF inside another IF.
#
# Example:
num = 15

if num > 0:
    if num % 3 == 0:
        print("Positive and divisible by 3")
    else:
        print("Positive but not divisible by 3")
else:
    print("Not positive")


# ----------------------------------------------------------
# 5) COMMON BEGINNER MISTAKES
# ----------------------------------------------------------
# ❌ Using '=' instead of '==' in conditions 
# if x = 5:  # WRONG, '=' is assignment
# Correct:
# if x == 5:
#
# ❌ Forgetting colon ':'
# if x > 10   # WRONG
# if x > 10:  # CORRECT
#
# ❌ Wrong indentation (Python is indentation-sensitive)
#
# ❌ Writing conditions like:
# if (x > 10) { ... }  # WRONG (Python uses ':' and indentation, no braces {})


# ----------------------------------------------------------
# 6) REAL-WORLD EXAMPLES
# ----------------------------------------------------------

# Example 1: Login check
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Access denied")


# Example 2: Grading system
score = 87

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print("Grade:", grade)


# Example 3: Weather-based decision
temp = 32

if temp > 30:
    print("It's hot outside")
elif temp >= 20:
    print("Weather is pleasant")
else:
    print("It's cold")


# ----------------------------------------------------------
# 7) DSA-STYLE CONDITIONAL PROBLEMS
# ----------------------------------------------------------

# Problem 1:
# Check if a number is EVEN or ODD.
# Time Complexity: O(1)
def is_even(n):
    # % returns remainder
    if n % 2 == 0:
        return True
    else:
        return False

# Problem 2:
# Determine if a number is prime.
# Conditions + Loop (basic DSA)
# Time Complexity: O(n) simple method, better solutions exist.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Problem 3:
# Check maximum of 3 numbers using conditionals.
# Time Complexity: O(1)
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Problem 4:
# FizzBuzz Program (common interview question)
# If n % 3 == 0: print "Fizz"
# If n % 5 == 0: print "Buzz"
# If both: print "FizzBuzz"
# Time Complexity: O(1)
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

# Problem 5:
# Temperature conversion decision
# If scale == "C", convert C→F, else F→C.
def convert_temp(value, scale):
    if scale == "C":
        return (value * 9/5) + 32
    elif scale == "F":
        return (value - 32) * 5/9
    else:
        return None  # invalid scale


# ----------------------------------------------------------
# 8) MINI TEST CASES (ASSERTIONS)
# ----------------------------------------------------------
# These run only if this file is executed directly.

if __name__ == "__main__":
    print("\nRunning conditional code tests...\n")

    # Test is_even
    assert is_even(4) == True
    assert is_even(7) == False

    # Test is_prime
    assert is_prime(2) == True
    assert is_prime(9) == False

    # Test max_of_three
    assert max_of_three(10, 5, 2) == 10
    assert max_of_three(1, 9, 3) == 9

    # Test fizzbuzz
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"

    # Test convert_temp
    assert round(convert_temp(0, "C"), 2) == 32
    assert round(convert_temp(32, "F"), 2) == 0

    print("All tests passed successfully ✔️")

# ----------------------------------------------------------
# END OF FILE
# ----------------------------------------------------------
