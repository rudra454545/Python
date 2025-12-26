#2c)c)Write a program to find the factorial of a given number.
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    print(f"The factorial of {num} is {factorial(num)}")