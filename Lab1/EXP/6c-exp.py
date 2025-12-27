#6c)To create a text file and write data in it
user_data = input("Enter a supercar name to save: ")

file = open("supercars.txt", "w")
file.write(user_data)
file.close()

print("File created and data written.")