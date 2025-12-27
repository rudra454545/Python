#7a)Pickling data in Python.
import pickle

car_data = {"Model": "Phantom", "Brand": "Rolls-Royce", "Year": 2024}

with open("car_obj.dat", "wb") as f:
    pickle.dump(car_data, f)

print("Data has been pickled.")