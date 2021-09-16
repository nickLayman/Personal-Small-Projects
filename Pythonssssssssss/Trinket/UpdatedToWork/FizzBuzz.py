L = 1000
n = 1
while n <= L:
    p = ""
    if n % 3 == 0:
        p = p + "fizz"
    if n % 5 == 0:
        p = p + "buzz"
    if p == "":
        print(n)
    else:
        print(p)
    n += 1
