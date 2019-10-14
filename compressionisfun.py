# CompressionISFUN 
# i wrote this to show 
# that i can compress repitition
# over and over again with a lossless
# small program! Hit the Green
# run button and scroll to the
# top. The number and the 
# message are all created with
# this small program!!
# This is true lossless 
# compression. The integer it 
# creates is with math, no 
# tricks or anything, just
# using my compression
# algorithm!

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

j=-6
x=8
start=0
iterx=0
pattern="--+----------+-+-++---+-+-++---+--+--+-++--+--+++--+---+---+--+-+-++--+-+-++-----+-+-+--+-++-++++-++----+--+--+++--+--+-+++--+-++-"
lengthpattern=len(pattern)
for y in range (start+1, lengthpattern): 
   #print(iterx, j, pattern[y]) 
   if pattern[y]=='+':  
       p()  
   elif pattern[y]=='-':  
       n()  
   iterx+=1 
start=0
for c in range(0,500):
 for y in range (start+2, lengthpattern):
   #print(iterx, j, pattern[y]) 
   if pattern[y]=='+':  
       p()  
   elif pattern[y]=='-':  
       n()  
   iterx+=1
for y in range (start+2, lengthpattern-3):
   #print(iterx, j, pattern[y]) 
   if pattern[y]=='+':  
       p()  
   elif pattern[y]=='-':  
       n()  
   iterx+=1
message = abs(j) 
#print("Your numer in the universe is {}".format(message))

print("")
print("Your numer in the universe is {}".format(message))
print("")

print(bytes.fromhex(hex(int(str((abs(message))),10))[2:]))  

print("The above message is your compressed lossless data. Scroll to the top to see your number in the universe. It's compressesed 500 times with this small program!")
