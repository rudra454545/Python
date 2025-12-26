def check_palindrome():
    original_input = input("Enter a word or phrase: ")
    
    # Cleaning the string by removing spaces and making it lowercase
    cleaned_string = original_input.replace(" ", "").lower()
    
    # Comparing the string with its reverse
    if cleaned_string == cleaned_string[::-1]:
        print(f"Yes! '{original_input}' is palindrome.")
    else:
        print(f"No. '{original_input}' is not a palindrome.")

# Calling the function
check_palindrome()
