import time

while True:
    try:
        A = int(input('how big of a sample size?'))
    except ValueError:
        print
        'please input an integer'
        continue
    break
T1 = float(time.time())
L1 = []
L2 = []
L3 = []
L4 = []
L5 = []
L6 = []
import random

for X in range(A):
    X = random.randint(1, 6)
    if X == 1:
        L1.append(1)
    if X == 2:
        L2.append(1)
    if X == 3:
        L3.append(1)
    if X == 4:
        L4.append(1)
    if X == 5:
        L5.append(1)
    if X == 6:
        L6.append(1)
print(len(L1) / A)
print(len(L2) / A)
print(len(L3) / A)
print(len(L4) / A)
print(len(L5) / A)
print(len(L6) / A)
print('perfect=', 1 / 6)
T2 = float(time.time())
T = T2 - T1
print('this took', T, 'seconds')
A1 = len(L1) / A
A2 = len(L2) / A
A3 = len(L3) / A
A4 = len(L4) / A
A5 = len(L5) / A
A6 = len(L6) / A

import pygal

bar_chart = pygal.Bar()
bar_chart.title = 'frequency of random.randint'
bar_chart.x_labels = map(str, range(1, 7))
bar_chart.add('Frequency', [A1, A2, A3, A4, A5, A6])
bar_chart.render_in_browser()