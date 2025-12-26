
#a)Write a program to add two numbers.

try:
    num1= float(input ("Enter First Num"))
    num2= float(input ("Enter Second Num"))
    addition = num1 + num2
    print(f"The Addition of two numbers is: {addition}")
except ValueError:
    print("Error,Invalid Input. Give Numerics Only")