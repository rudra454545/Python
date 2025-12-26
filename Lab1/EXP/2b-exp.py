#b) Write a program to check if the string is a palindrome or not

def check_palindrome():
    original_input = input("Enter a word or phrase: ")
    

    cleaned_string = original_input.replace(" ", "").lower()
    
   
    if cleaned_string == cleaned_string[::-1]:
        print(f"Yes! '{original_input}' is palindrome.")
    else:
        print(f"No. '{original_input}' is not a palindrome.")


check_palindrome()
