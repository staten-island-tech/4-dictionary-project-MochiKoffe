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



for index, item in enumerate(solarballs):
    print(index, ":", item["name"], item["price"])

cart=[]
prices = []
purchasing = ""
money = ""


while purchasing != "done":
    purchasing = input("what will you like to buy (say done to stop)")
    cart.append(purchasing)
    money = float(input("gimme the cost of it boy (type '0' to finish: "))
    prices.append(money)
if 'done':
    input("do you wish to continue...")
elif 'yes': 
    input("thank you for your patronage...return for more peak")
elif 'no': 
    purhcasing = input("which solarballsballsballs you want")
    cart.append(purchasing)
    money = float(input("GIMME THE COST OF IT"))
    prices.append(money)
print(cart, prices)
total = sum(prices)

print(cart, total)
     
