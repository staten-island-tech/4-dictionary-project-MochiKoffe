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
    HONI = 0
    for i in range(len(word)):
        if word[i] == "H":
            H += 1
        if word[i] == "O":
            O += 1
        if word[i] == "N": 
            N += 1
        if word[i] == "I":
            I += 1
        if H+O+N+I % i == 1:
            HONI += 1
    print(H,O,N,I,HONI)
honi("MAGNUS")

""" def add (x,y):
    return x + y
result = print(add(5,6))
print(result) """