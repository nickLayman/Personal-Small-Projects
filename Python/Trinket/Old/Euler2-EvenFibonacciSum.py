a=1
b=2
c=0
l=4000000
while a<l and b<l:
  a+=b
  if b%2==0:
   c+=b
  if a<l and b<l:
   b+=a
   if a%2==0:
    c+=a
print c