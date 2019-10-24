# CompresssionIsBetterWithXORPatterns.py

# use python3 not python2
# This XOR pattern compresses
# to 35 bytes. xorpattern is
# only 35 bytes. With it we 
# acheive better compression
# than the newest gzip version
# By finding a pattern in XOR
# We can repeat this message
# many more times than gzip
# with much smaller size.
# gzip with 1000 repitiion
# is 144 bytes.
# To test you can take the 
# message and gzip and see
# that it is 144 bytes.


def n():
  global x, j
  j = j^-x
  x=x<<1

def p():
  global x, j
  j = j^x
  x=x<<1

what = b"CompresssionIsBetterWithXORPatterns"
j=1
x=2
xorpattern=1253701310082798857714472649037381798772545443176083147054309325165401383010204792462
pattern = bin(xorpattern)[2:]
repetition=1000
for y in range(0,repetition):
  if y != repetition-1:
     lenpattern = len(pattern)
  else:
     lenpattern = len(pattern) -1
  for c in range(0,lenpattern):
    if pattern[c]=='1':
       n()
    elif pattern[c]=='0':
       p()
message = j 
print(bytes.fromhex(hex(int(str((abs(message))),10))[2:])) 
      
