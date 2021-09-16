print("0<rate<1")
A=float(input("rate/time:A"))
B=float(input("rate/time:B"))
X=float(input("starting A="))
Y=float(input("starting B="))
Q=1
P=2
while Q<=150 or P==1:
  D=X-X*A+Y*B
  E=Y+X*A-Y*B
  print("After", Q, "time")
  print("A=", D)
  print("B=", E)
  X=D
  Y=E
  Q+=1