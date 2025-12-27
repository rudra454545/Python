#6e)To perform reading & writing operations in a text file.
with open("process.txt", "w+") as f:
    f.write("Initial Data: Ferrari")
    f.seek(0)
    print("Reading first time:", f.read())
    f.write("\nUpdated Data: Lamborghini")
    f.seek(0)
    print("Reading after update:\n", f.read())
    