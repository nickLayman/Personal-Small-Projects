#a set of dials which turn independently and should have 1 solution to make true statements
first=["1","2","3","4","5","6"]
second=["*","*","-","/","+","+"]
third=["1","2","6","3","4","5"]
fourth=["/","+","*","-","-","+"]
fifth=["1","3","2","5","4","6"]
last=["3","4","2","5","6","1"]

all = [first, second, third, fourth, fifth, last]


def rotate(list):
  for x in range(0,6):
    list[x]=list[(x+1)%6]

def rotateAll():
  for x in range(0, 6):
    rotate(all[x])

def evaluate(x):
  return(first[x] + second[x] + third[x] + fourth[x] + fifth[x] + "==" + last[x])
  
def evaluateAll():
  for x in range(0,6):
    print(evaluate(x))

evaluateAll()
rotateAll()
evaluateAll()