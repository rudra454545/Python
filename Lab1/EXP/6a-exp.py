#6a)Writing and reading to a text file

file_name = "data.txt"
content = "Bugatti Chiron\nKoenigsegg Jesko"

with open(file_name, "w") as f:
    f.write(content)

with open(file_name, "r") as f:
    print(f.read())