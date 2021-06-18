# empty_list = []

# Cities
cities_list = ["Oakland", "Atlanta", "New York City", "Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]
print(cities_list)

# print 3 cities
print(cities_list[0])
print(cities_list[3])
print(cities_list[5])

three_cities = cities_list[3:6]
print(three_cities)

# list slicing -> 4 items
four_cities = cities_list[0:4]
print(four_cities)

# replace cities
cities_list[0] = "San Francisco"
cities_list[2] = "Brooklyn"
cities_list[7] = "Hollywood"
cities_list[5] = "Tampa"
print(cities_list)

# add cities
cities_list.append("New Jersey")
cities_list.extend(["Santa Cruz", "Selma", "Chicago"])
cities_list.insert(7, "Washington D.C.")
cities_list.append("Oakland")
cities_list.extend(["New York City", "Los Angeles"])
cities_list.insert(0, "Miami")
print(cities_list)

# remove cities
del cities_list[8]
cities_list.pop(4)
cities_list.remove("Miami")
print(cities_list)

# Fruits
fruit_list = ["Apple", "Banana", "Orange", "Pear", "Tomato", "Plum", "Kiwi", "Strawberry", "Blueberry", "Raspberry"]
print(fruit_list)

# list slicing -> four fruits
four_fruits = fruit_list[4:8]
print(four_fruits)
