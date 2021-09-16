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


while True:
    try:
        U = int(input('How many?'))
    except ValueError:
        print('please input an integer')
        continue
    break
while True:
    x = 3
    L = [1, 2]
    while len(L) < U:
        if f(x) == 0:
            L.append(x)
        x += 2
    print(L)
    break
T = 0
Difs = []
for A in range(U - 1):
    D = (L[A + 1] - L[A])
    T += D
    Difs.append(D)
AV = T / U
print('Average difference=', AV)
import pygal

line_chart = pygal.Line()
line_chart.title = 'Differences between primes'
line_chart.x_labels = map(str, range(U - 1))
line_chart.add('dif.', Difs)
line_chart.render()
