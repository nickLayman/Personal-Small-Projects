import matplotlib.pyplot as plt
import numpy as np

def arithmetric(a, b, delta):
	a, b = min(a, b), max(a, b)
	while b-a > delta:
		b = (a+b)/2
		a = np.sqrt(a*b)
	return a


s = [10] # np.linspace(1, 10000, 11)
t = np.linspace(1, 1000, 1000)

for a in s:
	vals = []
	for b in t:
		vals.append(arithmetric(a, b, 0.01))
	plt.plot(t, vals, label=a)

x1, x2 = 500, 1000
y1, y2 = arithmetric(s[0], x1, 0.01), arithmetric(s[0], x2, 0.01)
m = (y2-y1)/(x2-x1)
plt.plot(t, m*(t-x1)+y1)

print(x1, y1, x2, y2, m)

plt.legend()
plt.show()