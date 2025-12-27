#7b)Unpickling data in Python.
import pickle

try:
    with open("car_obj.dat", "rb") as f:
        loaded_data = pickle.load(f)
        print("Unpickled Data:", loaded_data)
except FileNotFoundError:
    print("Binary file not found.")