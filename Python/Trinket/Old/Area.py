import math
x=input("Which?\n 1:Rectangle\n 2:Triangle\n 3:Circle\n 4:Trapezoid\n 5:Parallelogram\n 6:Regular Polygon\n")

if x=="1" or x=="Rectangle" or x=="1:Rectangle":
  L=float(input("length?"))
  W=float(input("width?"))
  print"Area=", L*W

if x=="2" or x=="Triangle" or x=="2:Triangle":
  y=input("Given?\n 1:Base and Height?\n 2:side lengths\n")

  if y=="1" or y=="Base and Height" or y=="1:Base and Height":
    B=float(input("base?"))
    H=float(input("Height?"))
    print"Area=", B*H/2

  if y=="2" or y=="side lengths" or y=="sides" or y=="1:side lengths":
    A=float(input("side 1="))
    B=float(input("side 2="))
    C=float(input("side 3="))
    H=.5*(A+B+C)
    A=math.sqrt(H*(H-A)*(H-B)*(H-C))
    print"Area=", A

if x=="3" or x=="Circle" or x=="3:Circle":
  R=float(input("Radius?"))
  A=3.141592654*R**2
  print"Area=", A 

if x=="4" or x=="Trapezoid" or x=="4:Trapezoid":
  B1=float(input("Base 1?"))
  B2=float(input("Base 2?"))
  H=float(input("Height?"))
  A=H*(B1+B2)/2
  print"Area=", A

if x=="5" or x=="Parallelogram" or x=="5:Parallelogram":
  L=float(input("Length?"))
  H=float(input("Height?"))
  A=L*H
  print"Area=", A

if x=="6" or x=="Regular Polygon" or x=="6:Regular Polygon":
  C=input("Apothem known?\n 1:no\n 2:yes\n")

  if C=="no" or C=="1" or C=="1:no":
    N=int(input("how many sides?"))
    x=input("Given?\n 1:side length \n 2:circumradius\n")

    if x=="1" or x=="side length" or x=="1:side length":
      s=float(input("side length"))
      A=(s/(2*math.tan(3.141592654/N)))
      print "Apothem=", A
      P=float(input("Perimeter?"))
      print"Area=", P*A/2

    if x=="2" or x=="circumradius" or x=="2:circumradius":
      R=float(input("circumradius?"))
      print("Apothem=", (R*math.cos(3.141592654/N)))

  if C=="yes" or C=="2" or C=="2:yes":
    A=float(input("Apothem?"))
    P=float(input("Perimeter?"))
    print"Area=", P*A/2