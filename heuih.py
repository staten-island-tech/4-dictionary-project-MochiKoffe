solarballs = [ 
{
    "name": "Benus",
    "price": 42.670,
    "department": "planet",
    "description": "VENUSS PLANET OF LOVEEEE WAS DESTROYED BY GLOBAL WARMINGGGGGGG GHAIUEHGUIEH I LOVE VENUS"
}, 
{
    "name": "SUNNNN",
    "price": 718973589759189,
    "department": "star",
    "description": "THE CENTER OF OUR SOLAR SYSTEM SUNNNNMY BABYYYYY"
},
{
    "name": "neptune",
    "price": 7238597,
    "department": "ice giant",
    "description": "GODS I LOVE NEPTUNE MY NEPTUNEAEIUFNUIEAF"
},
{
    "name": "EARTH",
    "price": 12478949817893719573817598,
    "department": ["only habital planet", "rocky"],
    "description": "Do NOTTTTT GO into the sun we are all gonna DIE EARTH HELPPPPPPPP"
},
]


""" print(solarballs[0]["name"])
print(solarballs[1]["description"])
print(solarballs[2]["name"]) """


""" for index, item in enumerate(solarballs):
    print(index, ":", item["name"], item["department"], item["description"]) """

""" def showItems(items): 
    for index, item in enumerate (items): 
        print(index,":", item["name"])
def thing(): 
    showItems(solarballs)
    x = int(input("buy?"))
    print(solarballs[x])
showItems(solarballs) 
print(solarballs[0])
thing() """



for index, item in enumerate(solarballs):
    print(index, ":", item["name"], item["price"]) #print dictionary

cart=[]
total = 0 #variables to print at the end


purchasing = int(input("buy?")) #question
cart.append(solarballs[purchasing]) #add item (all of info) into cart
print(cart)
total += solarballs[purchasing]['price'] #add the price of it to the total

while True: #if the loop doesnt break
    checkout = input("Do you wish to continue shopping?(yes/no)") #continue shopping?
    if checkout == "yes": #if yes
        purchasing = int (input("What else would you like to buy?")) #repeat original code
        cart.append(solarballs[purchasing])
        print(cart)
        total += solarballs[purchasing]['price']
    elif checkout == "no": #if no
        break #break the loop, making it false
    else: #unnecessary
        print("say yes/no")

for item in cart: #in the cart for each item, print the name and its price
    print(f"{(item['name'])}, ${float(item['price'])}") #print each ones name and price as a float (f formats the string so it is "name, $price")
print(f"Total: ${total}") #print what the total is