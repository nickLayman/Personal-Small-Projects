def convertDecToBinary(n):
    if n < 2:
        return n
    else:
        return str(int(convertDecToBinary(int(n/2)))) + str(int(n % 2))


def convertDecToBase(n, b):
    if n < b:
        return n
    else:
        return str(int(convertDecToBase(int(n/b), b))) + str(int(n % b))


for x in range(0, 65):
    print(convertDecToBase(x, 4))
