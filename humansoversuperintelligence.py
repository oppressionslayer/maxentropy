
# xxPostxx


def Xploder(s):
  if s==-1:
    return 0
  elif s==0:
    return 1
  elif s %2 == 0:
    return ((s*2))+1
  elif s==2:
    return 2
  else:
    #for x in range(0,10):
    temp = s+1
    #print(s,temp)
    s = temp * 2 -1
    return s


def exploder(s):
  if s % 2 == 0 and s != 2:
    return s-1
  elif s==2:
    return 2
  else:
    #for x in range(0,10):
    temp = s+1
    #print(s,temp)
    s = temp * 2 -1
    return s


def getnexthex(hm):
  a=0
  f=''
  hm = hex(hm)
  hmlen = len(hm) -4
  for x in range(0,hmlen):
    f += 'f'
  hm = int(hm,16) ^ int(str(hm[2] + f + 'e'),16)
  return hm


def printssx(j, s,y, previ, h, ssx, number): 
    hy = h^y 
    hs = h^s 
    if hs == 0: 
      hs = h 
    hs1 = h^s+1 
    hssx1 = h^ssx+1 
    previh = previ^h 
    if previh == 0: 
       previh=h 
    sabsjyj= s^abs(j-(y^j)) 
    ssxabsjyj = ssx^abs(j-(y^j)) 
    if s^y==0: 
       syhsy= s,h^(s^y) 
    else: 
       syhsy= s^y,h^(s^y) 
    ssxyhsssxy = (exploder(ssx)^y),h^(ssx^y) 
    hyyy1y12y14= (h^y)^((y^y+1)+((y+1)*2)+((y+1)*4)) 
    print(s,y, ssx, h, hy, hs, hs1,previh, sabsjyj, hssx1, ssxabsjyj, ssxyhsssxy, hyyy1y12y14, 1)  
    print(s,y, ssx, h, hy, hs, hs1,previh, sabsjyj, hssx1, ssxabsjyj, syhsy, hyyy1y12y14, 2)  
    print(s,y, exploder(exploder(ssx)), h, hy, hs, hs1,previh, sabsjyj^exploder(exploder(s)), hssx1^exploder(exploder(ssx)), ssxabsjyj^exploder(exploder(ssx)), ssxyhsssxy[0]^exploder(exploder(ssx)), ssxyhsssxy[1]^exploder(exploder(ssx)),hyyy1y12y14^exploder(exploder(h)), 3) 
    print(s,y, exploder(ssx), h, hy, hs, hs1,previh, sabsjyj^exploder(s), hssx1^exploder(h), ssxabsjyj^exploder(ssx), ssxyhsssxy[0]^exploder(ssx), ssxyhsssxy[1]^exploder(ssx),hyyy1y12y14^exploder(h), 4) 
  

def getintandec(hm):
  return hm, hex(hm)

# Firt random numbers of AMillionRandomDigits.bin : 1009732533765201
# We use getnexthex to generate 116167373077422, from 1009732533765201 and you will see that you get the answer
# in the form of 2019465067530403  which //2 is 1009732533765201
# The anomaly also works for just 1009. Try it, change j to j=getnexthex(1009)-1 and you will get the answer
# Also this will get you the next prime for 1009732533765201 which is 1009732533765251. Try it, the  //2 answer is
# the prime. And guess what, we didn't start with that number, we get it from a number which is the getnexthex
# of the answer. 

# Very cooly, there is a XOR relationship with the answers above and below the numbers in these columns. They are
# the powers of 2 numbers. You can verify by doing your xors in getintanddec(): like this:
# In [14]: getintandec(2019465067530503^232334746154744)                                                                                                                                                                                                                               
# Out[14]: (2251799813685247, '0x7ffffffffffff')
#
#  I believe we can beat entropy, by discovering a hidden order between numbers that is unaccounted for. I believe a
# supercomputer can solve this, but we are humans, and if we put our minds to it, we can be the worlds first superintelligences
#  Is there anyone willing to work with me for this monunmental acheivement? I have a version of this program that is so 
# awesome, that i can get the next answer to every output, using a doubling of the previous result, getting all the way
# to the answer i want, except for one catch. sometimes, the results are negative. But i don't know how to account for that
# i just know that you can walk down the tree, each time, by just doubling the answer and using XOR and getting to the orignal # result from a getnexthex number of your result. That is impressive. What i am noticing is that negative seems to be occuring
# when the XOR chain converges on a powers of 2 number i.e. ( 2**50 ) and such.
#
# I do have some unnecessary prints, but this helps me when walking down the XOR chain. My end goal is to get the next value
# by just doubling a number, that gets the next result. I'm close. I just need help. Collobaration will get this done. Please
# collborate with me if you are impressed by this. Thanks.

# Try each of these j= results, by uncommenting the others and see you get the answer, in a semi walkdown XOR tree.

# No one can patent this method, i am open sourcing the use of using a XOR walk down tree.

# The 9th column is the cool one. Remember to use getintdec(result^previous) to see the walkdown from a powers of two number - # 1

# Sample output: column 9: 2019465067530503  which //2 is 1009732533765251 (next prime of 1009732533765201)
# Sample output column 9: 2019  which //2 is 1009 ( which is the first digits of AMillionRandomDigits, which is already prime)
# Sample output column 9:  2019465067530403  ( which //2 is 1009732533765201, the exact numbers of  AMillionRandomDigits )
# Sample output column 9: getintanddec(2019465067530403^232334746154844) which is (2251799813685247, '0x7ffffffffffff') and 
# is in the first column, because i iterate powers of 2 to get these results. Cool huh?

# Use ipython to run this, it's a quick way to run the program.

# Mark Nelson. I have learned so much about you Random number, i think i may know so much about it, that i can share info about
# it that would impress you. Even though i believe you created this challenge to prove entropy, i have immense appreciation for # for your random number, and i think i have in the past few years, learned and studied it so much that i think i'm on the
# verge of doing what frustrates mathemeticians, the ability to find a XOR path walking down a tree to get an answer just by   # doubling
# a previous result for each iteration. I think you might appreciate this and that people are working hard on launching the new
# information age. You must know that one day a superintelligence will find this XOR tree. What not it be us? Humans, and not
# an AI.

def humansoversuperintelligence(j, y, s, ssx):
 y=127 #127
 s=127 # #1923
 ssx=4
 j=getnexthex(j)-1  # Which is 14. From 14 we get to 2019, which //2 is 1009. Cool huh?
 #j=getnexthex(1009732533765251)-1  # Which is 116167373077372. and in 9th column is the answer if we div/2 Cool huh?
 #j=getnexthex(1009732533765201)-1 # Which is 116167373077422. and in the 9th column is the answer if we div/2 Cool huh?
 h=j
 h=getnexthex(j)
 previ=abs(j-(y^j))
 breakit = 0
 for x in range(0,200):
   for xx in range(0,2): 
     if xx == 0:
       printssx(j, s,y,previ,h, ssx, 1)
       previ=h
       h = abs(getnexthex(j) -(y^getnexthex(j)))
       printssx(j, s,y,previ,h, ssx, 2)
       y=Xploder(y) #y*2)+1
     if xx == 1:
       printssx(j, s,y,previ,h, ssx, 0)
       previ=h
       h = abs(getnexthex(j) -(s^getnexthex(j)))
       printssx(j, s,y,previ,h, ssx, 4)
       s=Xploder(s)
       ssx=Xploder(ssx)
   printssx(j, s,y,previ,h, ssx, 4)
   if breakit == 1:
     break
   if len(str(h)) > len(str(j)):
     breakit+=1

humansoversuperintelligence(1009, 127, 127, 4) 
humansoversuperintelligence(1009732533765251, 127, 127, 4) 
humansoversuperintelligence(1009732533765201, 127, 127, 4) 

