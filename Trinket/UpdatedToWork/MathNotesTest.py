def factorial(x):  # factorial max = ~1860
    if x == 0:
        return 1
    else:
        x = x * factorial(x - 1)
        return x


def factorials(x):  # factorial max = ?
    f = 1
    while (x > 1):
        f = f * x
        x = x - 1
    return f


print('''Use triple quotes
for a multiline
print statement''')  # multiline print

x = "hello"  # using variables for printing.
y = "World"  # using commas gives an automatic
print("use variables to print", x, y)  # space between statements
print("or plus signs to print" + " " + x + " " + y ) # Plus signs do NOT add spaces
print("'%' and 's' with '.format' to print %s %s" % (x, y))  # order matters; variables added in later
print("I am printing {} {}".format(x, y))  # remember the period; brackets will be filled in in order if nothing is in their arguments
print("I am printing",)  # adding a comma after the statement
print(x,)  # makes them all on
print(y)  # one line
print("i am printing {0} {y}".format(x, y=y))  # must start at 0; if variables inserted, they must be defined

import math  # Apothem program

N = 30
s = 1
A = (s / (2 * math.tan(3.141592654 / N)))  # must include 'math.' and import math earlier
print("Apothem=", A)

import time

print(time.time())
