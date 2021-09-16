L=[]
for x in range(1, 1000):
  print x, 'number'
  l=0
  while x!=1:
    if x%2==0:
      x=x/2
      l+=1
    else:
      x=(3*x+1)/2
      l+=2
  print l
  L.append(l)
print L
print 'Max =', max(L), 'iterations'
print L.index(max(L))+1, '=number'