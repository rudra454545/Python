#3a)Write a program to read a number and display the corresponding day of the week using if-elif.
try:
    day_num = int(input("Enter a number (1-7) for the day of the week: "))

    if day_num == 1:
        print("Day 1 is Sunday")
    elif day_num == 2:
        print("Day 2 is Monday")
    elif day_num == 3:
        print("Day 3 is Tuesday")
    elif day_num == 4:
        print("Day 4 is Wednesday")
    elif day_num == 5:
        print("Day 5 is Thursday")
    elif day_num == 6:
        print("Day 6 is Friday")
    elif day_num == 7:
        print("Day 7 is Saturday")
    else:
        print("Invalid Input! Please enter a number between 1 to 7.")

except ValueError:
    print("Invalid Input! Please enter a numeric value.")
