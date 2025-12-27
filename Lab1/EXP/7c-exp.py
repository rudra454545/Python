#7c)To perform basic operations on a binary file using pickle module

import pickle

def save_records():
    records = [
        {"ID": 1, "SUV": "Range Rover"},
        {"ID": 2, "SUV": "G-Wagon"}
    ]
    with open("suv_records.dat", "wb") as f:
        pickle.dump(records, f)

def read_records():
    with open("suv_records.dat", "rb") as f:
        data = pickle.load(f)
        for item in data:
            print(f"Record: {item}")

save_records()
read_records()