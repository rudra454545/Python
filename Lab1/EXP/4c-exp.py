#4c) Create a tuple and perform the following methods:Add item(), len(), Check for item in tuple, Access items
luxury_sedans = ("Rolls Royce Phantom", "Bentley Mulsanne", "Maybach S-class")

print("Original Tuple: ", luxury_sedans)

first_car = luxury_sedans[0]
last_car = luxury_sedans[-1]

print(f"\nFirst Item: {first_car}")
print(f"Last Item: {last_car}")

print(f"\nThe tuple contains {len(luxury_sedans)} luxury sedans.")

search_car = "Bentley Mulsanne"
if search_car in luxury_sedans:
    print(f"Yes, '{search_car}' is in the tuple.")
else:
    print(f"No, '{search_car}' is not in the tuple.")

temp_list = list(luxury_sedans)
temp_list.append("Aston Martin Rapide")
luxury_sedans = tuple(temp_list)

print("\nAfter adding a new item (via list conversion):")
print(luxury_sedans)
