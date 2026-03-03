""" def occupied (n,y,t):
    found = 0
    for i in range(n):
        if y[i] == "C" and t[i] == "C":
            found += 1
    print(found)
occupied(5,"CCC..","C..CC") """



""" def language (sentence):
    t=0
    T=0
    s=0
    S=0
    for i in range(len(sentence)):
        if sentence[i] == "t":
            t += 1
        if sentence[i] == "T":
            T += 1
        if sentence[i] == "s":
            s += 1
        if sentence[i] == "S":
            S += 1
    print(s, S, t, T)
    if t+T > s+S: 
        print("probably English")
    if s+S >= t+T:
        print("probably French")
language("The red cat sat on the mat. Why are you so sad cat? Don't ask that.")
language("The redsssssssssssssssss") """


def honi (word): 
    H=0
    O=0
    N=0
    I=0
    current = "H"
    HONI = 0
    for i in range (len(word)):
        if word[i] == current:
            H += 1
        current == "O"
        if word[i] == current:
            O += 1
        current == "N"
        if word[i] == current: 
            N += 1
        current == "I"
        if word[i] == current:
            I += 1
        if H+O+N+I == 4:
            HONI += 1
            H=0
            O=0
            N=0
            I=0
            current = "H"
        else: 
            HONI == 0
    print(HONI)
honi("PROHODNIHODNIK")
honi("HHHHOOOONNNNIIII")
honi("MAGNUS")

""" def add (x,y):
    return x + y
result = print(add(5,6))
print(result) """