# goal = 100973253376520135  from RAND's AMillionRandomDigits.bin. 

d={}
for x in range(0,32):
  d[str(x)]=[]
for x in range(0,100): 
  d[str(len(str(2**x)))].append(2**x-1)


# goal = 100973253376520135  from RAND's AMillionRandomDigits.bin. 


prime=56 
y=4095 
breakit=prime
for x in range(0,40): 
     #print(x, y, prime, prime^y) 
     prime=prime^y 
     breakit=breakit-1
     y=y^y+1 
     if y ==  d['6'][2]:
         y=d['7'][0]
     if y==d['13'][3]:
        prime=prime^(1181*2**25-1)
        breakit = 1
     if breakit == 0:
        break
     #print(x, y, prime, prime^y) 
prime=prime^d['14'][2]
prime=prime^(717*2**47)
print(prime)
