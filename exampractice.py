""" def occupied (n,y,t):
    found = 0
    for i in range(n):
        if y[i] == "C" and t[i] == "C":
            found += 1
    print(found)
occupied(5,"CCC..","C..CC")



def language (sentence):
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
language("The redsssssssssssssssss")


def magnus(word):
    count = 0
    state = 0

    for char in word: 
        if state == 0 and char.upper() == "H":
            state = 1
        elif state == 1 and char.upper() == "O":
            state = 2
        elif state == 2 and char.upper() == "N":
            state = 3
        elif state == 3 and char.upper() == "I":
            state = 0
            count += 1
    print(count)
magnus("HHHHOOOONNNNIIII")
magnus("MAGNUS")
magnus("PROHODNIHODNIK") """


""" def multi (number, answers, correct): 
    right = 0
    for i in range (len(answers)): 
        if answers[i] == correct[i]: 
            right += 1
    print(right)
multi(3, "AAA", "ABA")
multi(3, "ACB", "ABC") """

""" def check_password(password): 
    upper_check = 0
    lower_check = 0
    digit_check = 0
    for char in password: 
        if char.isUpper():
            upper_check += 1
    if len(password) > 8 and len(password) < 12: 
        if upper_check > 3 and lower_check > 1 and digit_check > 1: 
            print('valid') """


def megabyte (mega, months, usage):
    value = mega
    for i in range(months): 
        if value > 0: 
            value -= usage[i]
            value += mega
    print(value)
megabyte(10, 3, [4,6,2])


""" def add (x,y):
    return x + y
result = print(add(5,6))
print(result) """