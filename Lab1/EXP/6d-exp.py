#6d)To display data from a text file.
try:
    with open("supercars.txt", "r") as file:
        data = file.read()
        print("File Content:", data)
except FileNotFoundError:
    print("Error: File does not exist.")