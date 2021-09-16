z = 0
a = 0
b = 0
c = 0
d = 0
e = 0
while e < 4:
    while a < 4:
        while b < 4:
            while c < 4:
                while d < 4:
                    print(e, a, b, c, d)
                    d += 1
                    z += 1
                d = 0
                c += 1
            d = 0
            c = 0
            b += 1
        d = 0
        c = 0
        b = 0
        a += 1
    d = 0
    c = 0
    b = 0
    a = 0
    e += 1
print(z)
