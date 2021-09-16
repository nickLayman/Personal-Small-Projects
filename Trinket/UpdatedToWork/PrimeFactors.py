import time


def factor(n):
    import math
    a = n
    p = 2
    L = [1]
    product = 1

    def factorials(x):
        f = 1
        while (x > 1):
            f = f * x
            x = x - 1
        return f

    def f(x):
        P = factorials(x - 1) + 1
        x = P % x
        return x

    while a % p == 0:
        if f(p) == 0:
            # print p
            L.append(p)
            product = product * p
            a = a / p
    p += 1
    while p < n / 2 and n != product:
        while a % p == 0:
            if f(p) == 0:
                # print p
                L.append(p)
                product = product * p
                a = a / p
        p += 2
    print(L)
    print(max(L))


while True:
    try:
        a = int(input('number='))
        break
    except ValueError:
        print("please input a number")
factor(a)
