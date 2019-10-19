def n():
  global x, j
  j = j^-x
  x=x<<1

j=0
x=2**1
for y in range(0,100000):
   n()
hex(j)
