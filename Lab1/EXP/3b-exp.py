#3b) Write a program that takes two lists and returns True if they are equal, otherwise False
def check_lists():
    
    list1 = input("Enter elements of the first list (separated by space): ").split()
    list2 = input("Enter elements of the second list (separated by space): ").split()

    print(f"\nList 1: {list1}")
    print(f"List 2: {list2}")

   
    if list1 == list2:
        return True
    else:
        return False


result = check_lists()
print(f"Are the lists equal? {result}")