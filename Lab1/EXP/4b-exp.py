# 4b) Create a dictionary and apply the following methods: 
#     Print the dictionary items, Access items, Use get(), Change values(), Use len()
suvs = {
    "Range Rover Autobiography": "Land Rover",
    "G Wagon": "Mercedes-Benz",
    "Cullinan": "Rolls-Royce",
    "Urus": "Lamborghini",
    "Defender": "Land Rover"
}

print("--- Dictionary Items ---")
print(suvs.items()) 
print("Full Dictionary:", suvs)

model = "G Wagon"
brand = suvs[model]
print(f"\nAccessing via brackets: The {model} is made by {brand}.")

suv_search = "Cullinan"
brand_search = suvs.get(suv_search)
print(f"Accessing via get(): The {suv_search} is made by {brand_search}.")

print("\nChanging value for 'Urus'...")
suvs["Urus"] = "Lamborghini (Performance Division)"
print("Updated Dictionary:", suvs)

count = len(suvs)
print(f"\nTotal number of SUVs in the dictionary: {count}")