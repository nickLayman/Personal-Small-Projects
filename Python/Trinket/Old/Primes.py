def factorials(x):
  f=1
  while(x>1):
    f=f*x
    x=x-1
  return f
P=1
def f(x):
  P=factorials(x-1) + 1
  x=P%x
  return x
for P in range(1, 101):
  if f(P)==0:
    print P
while True:
  try:
    C=int(input("Number?"))
    break
  except ValueError:
    print "must be an integer"
    continue
if f(C)==0:
  print"Prime"
else:
  print"composite"