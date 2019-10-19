def p():
  global x, j
  j = j^x
  x=x<<1

def n():
  global x, j
  j = j^-x
  x=x<<1

j=0
x=2**1
t='++-+-+------'
s=25000
for y in range(0,len(t*s)):
   if (t*s)[y] == '+':
      p()
   else:
      n()
hex(j)
