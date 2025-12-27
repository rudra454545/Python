#4a) Create a list and perform the following methods:
# insert (), remove (), append (), len(), pop(), clear()

supercars = ["Ferrari 296 GTB", "Lamborghini Revuelto", "McLaren 750s"]
print("Initial list: ", supercars)

supercars.append("Bugatti Tourbillon")
print("\nAfter append('Bugatti Tourbillon'): ", supercars)

supercars.insert(1, "Porsche 911 GT3 RS")
print("\nAfter insert(1, 'Porsche 911 GT3 RS'): ", supercars)

total_cars = len(supercars)
print(f"Current total number of cars: {total_cars}")

supercars.remove("McLaren 750s")
print("\nAfter remove('McLaren 750s'): ", supercars)

popped_car = supercars.pop(0)
print(f"After pop(0) : {supercars}")
print(f"The car that was 'popped' (removed) was : {popped_car}")

supercars.clear()
print("\nAfter clear(): ", supercars)
