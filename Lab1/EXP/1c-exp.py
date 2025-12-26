
#c)Write a program to find the largest number among three numbers.

try:
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    n3 = float(input("Enter the 3rd number: "))
    
    largest = max(n1, n2, n3)
    print(f"The largest number is: {largest}")

except ValueError:
    print("Error, Invalid input, enter a numeric")
