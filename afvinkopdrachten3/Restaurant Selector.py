restaurants = ["Joe's Gourmet Burgers", "Main Street Pizza Company", "Corner Café", "Mama's Fine Italian",
               "The Chef's Kitchen"]
vegetarian = input("Is anyone at your party a vegetarian? Type yes or no: ")
if vegetarian == "yes":
    restaurants.remove("Joe's Gourmet Burgers")
vegan = input("Is anyone at your party a vegan Type yes or no: ")
if vegan == "yes":
    if not "Joe's Gourmet Burgers" in str(restaurants):
        restaurants.remove("Main Street Pizza Company")
        restaurants.remove("Mama's Fine Italian")
    else:
        restaurants.remove("Joe's Gourmet Burgers")
        restaurants.remove("Main Street Pizza Company")
        restaurants.remove("Mama's Fine Italian")
gluten = input("Is anyone at your party gluten-free? Type yes or no: ")
if gluten == "yes":
    if not "Joe's Gourmet Burgers" in str(restaurants) and not "Mama's Fine Italian" in str(restaurants):
        print("")
    elif not "Joe's Gourmet Burgers" in str(restaurants):
        restaurants.remove("Mama's Fine Italian")
    elif not "Mama's Fine Italian" in str(restaurants):
        restaurants.remove("Joe's Gourmet Burgers")
    else:
        restaurants.remove("Joe's Gourmet Burgers")
        restaurants.remove("Mama's Fine Italian")
print("--------------------------------------------------------")
for x in restaurants:
    print(x)