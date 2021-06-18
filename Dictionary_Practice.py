food_prices = {"Chicken": 1.59, "Beef": 1.99, "Cheese":1.00, "Milk": 2.50}

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
del NBA_players["Kevin Durant"]
del NBA_players["Bob"]
print(NBA_players)


