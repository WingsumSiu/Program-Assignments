food_prices = {"Chicken": 1.59, "Beef": 1.99, "Cheese": 1.00, "Milk": 2.50}

# food price dictionary
chicken_price = food_prices["Chicken"]
beef_price = food_prices["Beef"]
cheese_price = food_prices["Cheese"]
milk_price = food_prices["Milk"]
print(chicken_price, beef_price, cheese_price, milk_price)

# fruit color dictionary
fruit_color = {"Apple": "Red", "Pear": "Green", "Banana": "Yellow", "Apricot": "Orange"}

apple_color = fruit_color["Apple"]
pear_color = fruit_color["Pear"]
banana_color = fruit_color["Banana"]
apricot_color = fruit_color["Apricot"]
print(apple_color, pear_color, banana_color, apricot_color)

# change apple color
fruit_color["Apple"] = "Green"
apple_color = fruit_color["Apple"]
print(apple_color, pear_color, banana_color, apricot_color)

# nba players dictionary
NBA_players = {"Lebron James": 23, "Kevin Durant": 35, "Stephen Curry": 30, "Damian Lillard": 0}
NBA_players["Lebron James"] -= 17
print(NBA_players["Lebron James"])
NBA_players["Luka Doncic"] = 77
print(NBA_players["Luka Doncic"])

# shoe stock dictionary
shoe_stock = {"Jordan 13": 1, "Yeezy": 8, "Foamposite": 10, "Air Max": 5, "SB Dunk": 20}

jordan13_stock = shoe_stock["Jordan 13"]
yeezy_stock = shoe_stock["Yeezy"]
foamposite_stock = shoe_stock["Foamposite"]
airmax_stock = shoe_stock["Air Max"]
sbdunk_stock = shoe_stock["SB Dunk"]
print(jordan13_stock, yeezy_stock, foamposite_stock, airmax_stock, sbdunk_stock)

# purchase
sbdunk_stock -= 2
# return
yeezy_stock += 1
# new shipment
jordan13_stock += 7
yeezy_stock += 7
foamposite_stock += 7
airmax_stock +=7
sbdunk_stock += 7
# sale 
jordan13_stock -= 3
yeezy_stock -= 3
foamposite_stock -= 3
airmax_stock -= 3
sbdunk_stock -= 3
print(jordan13_stock, yeezy_stock, foamposite_stock, airmax_stock, sbdunk_stock)

# add 3 key: value pairs
#food_prices = {"Cereal": 3.25, "Gum": 1.50, "Carrot": 0.75}
food_prices["Cereal"] = 3.25
food_prices["Gum"] = 1.50
food_prices["Carrot"] = 0.75
print(food_prices)

#fruit_color = {"Plum": "Purple", "Kiwi": "Green", "Strawberry": "Red"}
fruit_color["Plum"] = "Purple"
fruit_color["Kiwi"] = "Green"
fruit_color["Strawberry"] = "Red"
print(fruit_color)

# I don't know basketball players...or shoes... :'(
#NBA_players = {"Bob": 2, "Sue": 7, "Albert": 21}
NBA_players["Bob"] = 2
NBA_players["Sue"] = 7
NBA_players["Albert"] = 21
print(NBA_players)

# delete items
del food_prices["Cheese"]
del food_prices["Milk"]
print(food_prices)
# del NBA_players["Kevin Durant"]
del NBA_players["Bob"]
print(NBA_players)


# Lab 4 - functions
# Step II 
def total_price(item1, item2):
    if item1 not in food_prices:
        return item1 + " doesn't exist in the dictionary"
    elif item2 not in food_prices:
        return item2 + " doesn't exist in the dictionary"
    else: 
        price1 = food_prices[item1]
        price2 = food_prices[item2]
        total_price = price1 + price2
        return "The total price of the " + item1 + " and the " + item2 + " is " + str(total_price)

def total_price2(item1, item2):
    if item1 not in food_prices:
        return item1 + " doesn't exist in the dictionary"
    elif item2 not in food_prices:
        return item2 + " doesn't exist in the dictionary"
    else: 
        price1 = food_prices[item1]
        price2 = food_prices[item2]
        total_price = price1 + price2
        return "The total price of the " + item1 + " and the " + item2 + " is " + str(total_price)
print(total_price("Chicken", "Beef"))

# Step III
def price_difference(item1, item2):
    if item1 not in food_prices:
        return item1 + " doesn't exist in the dictionary"
    elif item2 not in food_prices:
        return item2 + " doesn't exist in the dictionary"
    else: 
        price1 = food_prices[item1]
        price2 = food_prices[item2]
        price_difference = price1 - price2
        return("The price difference between the " + item1 + " and the " + item2 + " is " + str(abs(round(price_difference, 2))))

print(price_difference("Beef", "Chicken"))

# combined function
def price_total_and_difference(item1, item2):
    if item1 not in food_prices:
        return item1 + " doesn't exist in the dictionary"
    elif item2 not in food_prices:
        return item2 + " doesn't exist in the dictionary"
    else: 
        price1 = food_prices[item1]
        price2 = food_prices[item2]
        total_price = price1 + price2
        price_difference = price1 - price2
        return "The total price of the " + item1 + " and the " + item2 + " is " + str(total_price) + "\nThe price difference between the " + item1 + " and the " + item2 + " is " + str(abs(round(price_difference, 2)))
        
print(price_total_and_difference("Chicken", "Beef"))
print(price_total_and_difference("Chicken", "hello"))

# Step IV 
def restock(item, multiplier):
    if item not in shoe_stock:
        if item == "All":
            shoe_stock["Jordan 13"] = shoe_stock["Jordan 13"] * multiplier
            shoe_stock["Yeezy"] = shoe_stock["Yeezy"] * multiplier
            shoe_stock["Foamposite"] = shoe_stock["Foamposite"] * multiplier
            shoe_stock["Air Max"] = shoe_stock["Air Max"] * multiplier
            shoe_stock["SB Dunk"] = shoe_stock["SB Dunk"] * multiplier
            return shoe_stock
        else:    
            return item + " doesn't exist in the dictionary"
    else: 
        shoeinitial = shoe_stock[item]
        shoefinal = shoeinitial * multiplier        
        shoe_stock[item] = shoefinal
        return shoe_stock

print(restock("All", 4))
print(restock("Foamposite", 10))
print(restock("hey", 10))

# Step V
def clearance_sale(item, divisor):
    if item not in shoe_stock:
        if item == "All":
            shoe_stock["Jordan 13"] = shoe_stock["Jordan 13"] / divisor
            shoe_stock["Yeezy"] = shoe_stock["Yeezy"] / divisor
            shoe_stock["Foamposite"] = shoe_stock["Foamposite"] / divisor
            shoe_stock["Air Max"] = shoe_stock["Air Max"] / divisor
            shoe_stock["SB Dunk"] = shoe_stock["SB Dunk"] / divisor
            return shoe_stock
        else:    
            return item + " doesn't exist in the dictionary"
    else: 
        shoeinitial = shoe_stock[item]
        shoefinal = shoeinitial / divisor
        shoe_stock[item] = shoefinal
        return shoe_stock

print(clearance_sale("All", 4))
print(clearance_sale("Foamposite", 10))
print(clearance_sale("hi", 10))

# combined function (if no restock or final, the parameter would be 1)
def shoe_restock_clearance(item, multiplier, divisor):
    if item not in shoe_stock:
        if item == "All":
            shoe_stock["Jordan 13"] = shoe_stock["Jordan 13"] * multiplier / divisor
            shoe_stock["Yeezy"] = shoe_stock["Yeezy"] * multiplier / divisor
            shoe_stock["Foamposite"] = shoe_stock["Foamposite"] * multiplier / divisor
            shoe_stock["Air Max"] = shoe_stock["Air Max"] * multiplier / divisor
            shoe_stock["SB Dunk"] = shoe_stock["SB Dunk"] * multiplier / divisor
            return shoe_stock
        else:    
            return item + " doesn't exist in the dictionary"
    else: 
        shoeinitial = shoe_stock[item]
        shoefinal = shoeinitial * multiplier / divisor
        shoe_stock[item] = shoefinal
        return shoe_stock

print(shoe_restock_clearance("All", 8, 4))
print(shoe_restock_clearance("Foamposite", 10, 5))
print(shoe_restock_clearance("hello", 10, 5))

# Step VI 
def jersey_num_comparison_parity(player1, player2):
    jersey_num1 = NBA_players[player1]
    jersey_num2 = NBA_players[player2]
    comparison = ""
    jersey1_parity = ""
    jersey2_parity = ""

    if jersey_num1 > jersey_num2:
        comparison = str(player1) + "'s jersey number is greater than " + str(player2) + "'s jersey number."
    elif jersey_num1 < jersey_num2:
        comparison = str(player1) + "'s jersey number is smaller than " + str(player2) + "'s jersey number."
    else:
        comparison = str(player1) + "and " + str(player2) + "'s jersey number are the same."

    if jersey_num1 % 2 == 0:
        jersey1_parity = " " + str(player1) + "'s jersey number is an even number."
    else:
        jersey1_parity = " " + str(player1) + "'s jersey number is an odd number."

    if jersey_num2 % 2 == 0:
        jersey2_parity = " " + str(player2) + "'s jersey number is an even number."
    else:
        jersey2_parity = " " + str(player2) + "'s jersey number is an odd number."

    return comparison + jersey1_parity + jersey2_parity

print(jersey_num_comparison_parity("Stephen Curry", "Damian Lillard"))
print(jersey_num_comparison_parity("Lebron James", "Kevin Durant"))