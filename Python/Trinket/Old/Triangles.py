import math
x=input("Which?\n 1:Centroid\n 2:Area\n")
if x=="1" or x=="Centroid" or x=="1:Centroid":
  A=float(input("x[1]?"))
  B=float(input("y[1]?"))
  C=float(input("x[2]?"))
  D=float(input("y[2]?"))
  E=float(input("x[3]?"))
  F=float(input("y[3]?"))
  print"Centroid=({0}, {1})" .format((A+C+E)/3, (B+D+F)/3)
if x=="2" or x=="Area" or x=="2:Area":
  x=input("Given?\n 1:Vertex Coordinates\n 2:Side Lengths\n 3:Base and Height\n")
  if x=="1" or x=="Vertex Coordinates" or x=="1:Vertex Coordinates":
    A=float(input("x[1]?"))
    B=float(input("y[1]?"))
    C=float(input("x[2]?"))
    D=float(input("y[2]?"))
    E=float(input("x[3]?"))
    F=float(input("y[3]?"))
    D1=math.sqrt((C-A)**2+(D-B)**2)
    D2=math.sqrt((E-C)**2+(F-D)**2)
    D3=math.sqrt((E-A)**2+(F-B)**2)
    X=.5*(D1+D2+D3)
    a=math.sqrt(X*(X-D1)*(X-D2)*(X-D3))
    print"Area=", a
  if x=="2" or x=="Side Lengths" or x=="2:Side Lengths":
    A=float(input("Side 1?"))
    B=float(input("Side 2?"))
    C=float(input("Side 3?"))
    X=.5*(A+B+C)
    a=math.sqrt(X*(X-A)*(X-B)*(X-C))
    print"Area=", a
  if x=="3" or x=="Base and Height" or x=="3:Base and Height":
    B=float(input("Base?"))
    H=float(input("Height"))
    print"Area={}" .format(.5*B*H)