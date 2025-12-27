#3c) Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. 
#    If the score is between 0.0 and 1.0, print a grade

score_input = input("Enter Score (between 0.0 and 1.0): ")
try:
    score = float(score_input)
    if score < 0.0 or score > 1.0:
        print("Error, score is out of range. Please enter a value between 0.0 and 1.0.")
    elif score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")
except ValueError:
    print("Error: Invalid Input. Please enter numeric")
