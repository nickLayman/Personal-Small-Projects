import math

N = int(input("how many sides?"))
x = input("Given?\n 1:side length \n 2:circumradius\n")
if x == "1" or x == "side length" or x == "1:side length":
    s = float(input("side length"))
    A = (s / (2 * math.tan(3.14159265359 / N)))
    print("Apothem=", A)
if x == "2" or x == "circumradius" or x == "2:circumradius":
    R = float(input("circumradius?"))
    print("Apothem=", (R * math.cos(3.14159265359 / N)))
