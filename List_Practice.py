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

def city_name_printer():
    for i in range(0, len(cities_list)):
        print(cities_list[i])

city_name_printer()

def cities_list_organizer():
    for a in range(0, 100):
        for i in range(0, len(cities_list) - 1):
            #print(i)
            if len(cities_list[i]) < len(cities_list[i + 1]):
                x = cities_list[i]
                cities_list.remove(x)
                cities_list.append(x)
                #print(x)
    return(cities_list)

#print(len(cities_list))
print(cities_list_organizer())

def city_state_printer(city):
    if city not in cities_list:
        return city + " doesn't exist in the list."
    if city == "San Francisco":
        return city + " is in California."
    if city == "Atlanta":
        return city + " is in Georgia."
    if city == "Brooklyn":
        return city + " is in New York."
    if city == "Memphis":
        return city + " is in Tennessee."
    if city == "Tampa":
        return city + " is in Florida."
    if city == "Boston":
        return city + " is in Massachusetts."
    if city == "Hollywood":
        return city + " is in California."
    if city == "Denver":
        return city + " is in Colorado."
    if city == "New Orleans":
        return city + " is in Louisiana."
    if city == "New Jersey":
        return city + " is in New Jersey."
    if city == "Santa Cruz":
        return city + " is in California."
    if city == "Selma":
        return city + " is in Alabama."
    if city == "Chicago":
        return city + " is in Illinois."
    if city == "Oakland":
        return city + " is in California."
    if city == "New York City":
        return city + " is in New York."
    if city == "Los Angeles":
        return city + " is in California."
    

print(city_state_printer("Boston"))
print(city_state_printer("Oakland"))
print(city_state_printer("Selma"))
print(city_state_printer("New York City"))
print(city_state_printer("hello"))
