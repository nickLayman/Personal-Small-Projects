a = 0
b = 0
l = 1000
# while a<l:
#  if a%3==0 or a%5==0:
#    b+=a
#  a+=1
# print b
a = 0
b = 0
while a < l:
    a += 3
    if a % 5 == 0:
        a += 3
    if a < l:
        b += a
a = 0
while a < l:
    a += 5
    if a < l:
        b += a
print(b)
# about 2 times faster than brute force
