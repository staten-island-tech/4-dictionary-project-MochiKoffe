def occupied (n,y,t):
    found = 0
    for i in range(n):
        if y[i] == "C" and t[i] == "C":
            found += 1
    print(found)
occupied(5,"CCC..","C..CC")






""" y=("CCC..")
t=("...CC")
n=5
for i in range (n):
    n=i



def occupied (n,y,t):
    return n, y, t
print(occupied(5, "CCC..", "...CC")) """



""" def add (x,y):
    return x + y
result = print(add(5,6))
print(result) """