import random

A = 1
while True:
    try:
        L = int(input("Lower bound?\n"))
    except ValueError:
        print("Must be an integer")
        continue
    else:
        break
while True:
    try:
        U = int(input("Upper bound?\n"))
        if U < L:
            print('must be an integer greater than or equal to the lower bound')
            continue
    except ValueError:
        print("Must be an integer")
        continue
    else:
        break
while A == 1:
    X = random.randint(L, U)
    print(X)
    while True:
        try:
            A = int(input("Roll again?\n 1:Yes\n 2:No\n"))
        except ValueError:
            print("type '1' or '2'")
            continue
        if A != 1 and A != 2:
            print("type '1' or '2'")
            continue
        else:
            break
print("Ok, Bye!")
