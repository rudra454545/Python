## Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the 
## hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 
## hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to 
## read a string and float() to convert the string to a number.



hrs_input = input("Enter Hours: ")
rate_input = input("Enter Rate per Hour: ")

hrs = float(hrs_input)
rate = float(rate_input)

if hrs <= 40:
    pay = hrs * rate
else:
    regular_pay = 40 * rate
    overtime_hrs = hrs - 40
    overtime_pay = overtime_hrs * (rate * 1.5)
    pay = regular_pay + overtime_pay

print("Gross Pay:", pay)
