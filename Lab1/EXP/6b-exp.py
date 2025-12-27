#6b)Application of seek() and tell()

with open("seek_demo.txt", "w") as f:
    f.write("Luxury Cars")

with open("seek_demo.txt", "r") as f:
    print("Initial position:", f.tell())
    data = f.read(6)
    print("Read 6 bytes:", data)
    print("Position after read:", f.tell())
    f.seek(0)
    print("Position after seek(0):", f.tell())
    print("Re-reading from start:", f.read())