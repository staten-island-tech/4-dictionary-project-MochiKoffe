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
purchasing = ""
total = 0


while purchasing != "done":
    purchasing = input("what will you like to buy (say done to stop)")
    for i in solarballs:
        if purchasing == i: 
            cart.append(solarballs[i]["name"])
            total += solarballs[i]["price"]


if purchasing == "done":
    print("good choice *breakdances*,", cart, total)