#  This is true lossless compresssion. The
# integer than defines the message on the
# right after you hit run recreates that integer
# using math. Using math we recreate lossless
# compression, no tricks are used. This program
# without the header is about 596 bytes, and
# can recreate the integer of the actual
# message you see on the left. The goal was to 
# compress a repeating message losselessly and
# i obtained this goal by finding a repeating
# pattern that climbs to the original integer.
# This is a lossless self extracting compresser # of very small size

def n():
  global x
  global j
  temp = j^-x
  x=x<<1
  j = temp

def p():
  global x
  global j
  temp = j^x
  x=x<<1
  j = temp


j=5
x=8
pattern = "+-+----+--+------++++--++-+-+---"
lengthpattern = len(pattern)
firsttime = 1
for c in range(0,2500):
  start=0
  if firsttime == 1:
       start= 3
       firsttime = 0
  for y in range (start, lengthpattern):
    if pattern[y]=='+':
       p()
    elif pattern[y]=='-':
       n()
message = j 
print(bytes.fromhex(hex(int(str((abs(message))),10))[2:])) 
print("")
print("This number, recreated with this small program is in the universe as {}".format(abs(j)))
print("Scroll to the top to see the compressed message. This program is much smaller than the number it created and the message it compressed")
    
