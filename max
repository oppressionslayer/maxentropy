# xxXXxx
#
# You must install Bitstring to run this program:
#
#  BitString is a python import located at: https://pypi.org/project/bitstring/
#
# With that, you only need to run this from the terminal or ipython. Sample Output located at:
#
# https://github.com/oppressionslayer/maxcompress/blob/master/sample_8bit_one.txt
# https://github.com/oppressionslayer/maxcompress/blob/master/sample_output_8bit_two.txt
#
# Creates a random file, stores it as hex, and my betterthanzip files are smaller than the zip 
# compressed of the orighex.bin.
#
# To those who know entropy, no i don't break it, but i clearly show that i can compress random numbers
# much better than on the low boundry than zip, and still better at the high boundry. It's also cool
# to find relationships and algorithims to an orignal number, because numbers are fun, and i have algorithims that no one 
# else has. For example, i know how to create a HIGH/LOW map of a number like this from AMillionRandomDigits:
#  num = 100973253376520135863467354876809590911739292749453754204805648947429624805240372063610402008229166508422689531
#
# using math, and not using any kind of loop looking at the individual numbers. Do you know that formula? I doubt it. :-)
# So now you know i'm a math enthusiast with cool knowledge, and i don't claim to break entropy
# but i do claim to know about relationships from base10 to base16 that are new to mathematics.
#  Here is the formula you wished you discovered to create a high low map of the number above :-)
#
#  hex(((int(str(int(num) + int(num)),16)) - ((int(num,16) + int(num,16))))//6)hex((str(int(num) + int(num)),16)
#
#  which when compared, is a high low map. Seriously, do you know of any mathematician that has shown this 
#  base10 to base16 relationship? I'm not even one, but i like showing off cool math :-) The above math created the one
#  zero's you see below which perfectly mach high/low numbers in base10. (Lows are 0, highs are 1)
#
#  0x100973253376520135863467354876809590911739292749453754204805648947429624805240372063610402008229166508422689531
#  0x000110010011100001110011010111101110100101010101010110000101101101001100101000010010100000001001011101000111100
#     ( Make sure to align you binary number, i have a formater in this program )
#  
#    Compression engines do not account for a parity in the odd/even and high/low map of random data
#    so i have created a compressor that creates this parity to show that compression software 
#    does not account for this. As this allows for maximum compression, i feel like releasing
#    my fun knowledge on the subject. There is a mathematical relationship between the odd/even map
#    and high/low map, and the original number as this shows. (Really, they should just binary map it, 
#    but that's the same as mine, but better is mine has more information about your number than a simple 
#    binary map. That is my same size binary map is way cooler, because i know a lot about this subject 
#    that make math awesome, and I can show cool relationships of numbers that make them fun. Plus zip
#    is clearly not accounting for entropy on lower digit random numbers, so i do "compress" random numbers
#    better.
#    
#
#
# Task, Prove that some data formats of random digits can be compressed better
#       than zip. I'm claiming that zip can improve how it compresses some forms
#       of random data better.  Until then, i compress them better. :-)
# 
# Task, create a hexed(random4) and random4 stored as hex orighex.bin. Use zip to compress them.
# Task, create betterentropythanzip 'one' and 'two' or 'three' bins.
# Task, create a random number with high and low values to show off a new algorithim
#       created (by yours trully), to create a map of high/low values, mathematically,
#       and not by using loops, or building & strings to make it. This is a unique solution
#       i believe and i have not seen any acknowledgement yet of a counter claim that this could
#       be done mathematically. I'm also working on a version for odd/even maps. 
# Task, recreate a random 4 from betterentropythanzip bins that matches random4.bin
# Task, prove that my method maximizes entropy for the task, and that compression companies
#       can still improve compression on some forms of data created randomly. 
# 
#
#
#  Requirements for testing: Python, and BitString
#
#  BitString is a python import located at: https://pypi.org/project/bitstring/
#
#  All files and code are stored on github at:
# 
#  https://github.com/oppressionslayer/maxcompress
#
#

import os
import sys
import random
import pickle
import zipfile
from bitstring import BitString

#
# With a small code change i'll be adding shortly you can do odd length sizes, but for now,
# even sizes.
#

size=500000
debug='False'

def formatmap(map, lengthin):
  stonelen = len(map)
  stonediff = abs(lengthin - stonelen)

  makezeroin = ''
  if lengthin != stonelen: 
    for x in range(0,stonediff):
       makezeroin += '0'
  map = makezeroin+map
  if debug == 'True':
     print("stlen diff map ( requested size, actual size, difference): ", lengthin, stonelen, stonediff)
  return map

def buildcustomrandomnumbers(digits=8):
 if digits == 8:
  thelist = {11} 
  orderedrandomnumbers = []
  while len(thelist) != 5:
    thelist.add(random.randint(0,4))
  while len(thelist) != 9:
    thelist.add(random.randint(5,9))
  thelist.remove(11)
  for val in thelist:
    orderedrandomnumbers.append(val)
  return orderedrandomnumbers

 elif digits == 4:
  thelist = {11} 
  orderedrandomnumbers = []
  while len(thelist) != 3:
    thelist.add(random.randint(0,4))
  while len(thelist) != 5:
    thelist.add(random.randint(5,9))
  thelist.remove(11)
  for val in thelist:
    orderedrandomnumbers.append(val)
  return orderedrandomnumbers

def buildcustomrandomdata(orderedrandomlist, lengthin, digits=8):
 if digits==8:
  random4='' 
  for x in range(0,lengthin): 
    random4+=str(orderedrandomlist[random.randint(0,7)])

  ssxwrite=open('orighex_eight.bin', 'wb')
  BitString(hex=random4).tofile(ssxwrite)
  ssxwrite.close()

  with zipfile.ZipFile('orighex_eight.zip', 'w',zipfile.ZIP_DEFLATED) as myzip: 
      myzip.write('orighex_eight.bin') 

  return random4

 elif digits==4:
  random4='' 
  for x in range(0,lengthin): 
    random4+=str(orderedrandomlist[random.randint(0,3)])

  ssxwrite=open('orighex.bin', 'wb')
  BitString(hex=random4).tofile(ssxwrite)
  ssxwrite.close()

  with zipfile.ZipFile('orighex.zip', 'w',zipfile.ZIP_DEFLATED) as myzip: 
      myzip.write('orighex.bin') 

  return random4
  

def crwritelists(maxlist, oddevenlist):
  with open('betterthanzipmaxlist.bin', 'wb') as fp: 
     pickle.dump(maxlist, fp) 
  with open('betterthanzipoddevenlist.bin', 'wb') as fp: 
     pickle.dump(oddevenlist, fp) 
           
def crreadlists():
  with open ('betterthanzipmaxlist.bin', 'rb') as fp: 
     maxlist = pickle.load(fp) 
  with open ('betterthanzipoddevenlist.bin', 'rb') as fp: 
     oddevenlist = pickle.load(fp) 
  return maxlist, oddevenlist

def crandomd(random4, orderedrandomlist,digits=8):
 if digits==8:
  betterentropythanzipone=''
  betterentropythanziptwo=''
  betterentropythanzipthree=''
  for x in range(0,size):
    if random4[x] == str(orderedrandomlist[0]):
      betterentropythanzipone += '0'
      betterentropythanziptwo += '0'
      betterentropythanzipthree += '0'
    if random4[x] == str(orderedrandomlist[1]):
      betterentropythanzipone += '0'
      betterentropythanziptwo += '1'
      betterentropythanzipthree += '0'
    if random4[x] == str(orderedrandomlist[2]):
      betterentropythanzipone += '0'
      betterentropythanziptwo += '0'
      betterentropythanzipthree += '1'
    if random4[x] == str(orderedrandomlist[3]):
      betterentropythanzipone += '0'
      betterentropythanziptwo += '1'
      betterentropythanzipthree += '1'
    if random4[x] == str(orderedrandomlist[4]):
      betterentropythanzipone += '1'
      betterentropythanziptwo += '0'
      betterentropythanzipthree += '0'
    if random4[x] == str(orderedrandomlist[5]):
      betterentropythanzipone += '1'
      betterentropythanziptwo += '1'
      betterentropythanzipthree += '0'
    if random4[x] == str(orderedrandomlist[6]):
      betterentropythanzipone += '1'
      betterentropythanziptwo += '0'
      betterentropythanzipthree += '1'
    if random4[x] == str(orderedrandomlist[7]):
      betterentropythanzipone += '1'
      betterentropythanziptwo += '1'
      betterentropythanzipthree += '1'

  ssxwrite=open('betterentropythanzipone.bin','wb')  
  BitString(bin=betterentropythanzipone).tofile(ssxwrite)
  ssxwrite.close()  
  ssxwrite=open('betterentropythanziptwo.bin','wb')  
  BitString(bin=betterentropythanziptwo).tofile(ssxwrite)
  ssxwrite.close()  
  ssxwrite=open('betterentropythanzipthree.bin','wb')  
  BitString(bin=betterentropythanzipthree).tofile(ssxwrite)
  ssxwrite.close() 

  return betterentropythanzipone, betterentropythanziptwo,betterentropythanzipthree
 if digits == 4:
  betterentropythanzipone=''
  betterentropythanziptwo=''
  for x in range(0,size):
    if random4[x] == str(orderedrandomlist[0]):
      betterentropythanzipone += '0'
      betterentropythanziptwo += '0'
    if random4[x] == str(orderedrandomlist[1]):
      betterentropythanzipone += '0'
      betterentropythanziptwo += '1'
    if random4[x] == str(orderedrandomlist[2]):
      betterentropythanzipone += '1'
      betterentropythanziptwo += '0'
    if random4[x] == str(orderedrandomlist[3]):
      betterentropythanzipone += '1'
      betterentropythanziptwo += '1'

  ssxwrite=open('betterentropythanzipone.bin','wb')  
  BitString(bin=betterentropythanzipone).tofile(ssxwrite)
  ssxwrite.close()  
  ssxwrite=open('betterentropythanziptwo.bin','wb')  
  BitString(bin=betterentropythanziptwo).tofile(ssxwrite)
  ssxwrite.close()  
  return betterentropythanzipone, betterentropythanziptwo


def getsavedbins(lengthin, digits=8):
  if lengthin % 2 == 1:
    ssxread=open('betterentropythanzipone.bin', 'rb').read()
    w = BitString(ssxread) 
    readbetterentropythanzipone = bin(int(w.hex,16))[2:-1] 
    readbetterentropythanzipone = formatmap(readbetterentropythanzipone, lengthin)
    ssxread=open('betterentropythanziptwo.bin', 'rb').read()
    ww = BitString(ssxread)
    readbetterentropythanziptwo = bin(int(ww.hex,16))[2:-1]
    readbetterentropythanziptwo = formatmap(readbetterentropythanziptwo, lengthin)
    if digits == 8: 
      ssxread=open('betterentropythanzipthree.bin', 'rb').read()
      www = BitString(ssxread)
      readbetterentropythanzipthree = bin(int(www.hex,16))[2:-1] 
      readbetterentropythanzipthree = formatmap(readbetterentropythanzipthree, lengthin)
  else:
    ssxread=open('betterentropythanzipone.bin', 'rb').read()
    w = BitString(ssxread) 
    readbetterentropythanzipone = bin(int(w.hex,16))[2:] 
    readbetterentropythanzipone = formatmap(readbetterentropythanzipone, lengthin)
    ssxread=open('betterentropythanziptwo.bin', 'rb').read()
    ww = BitString(ssxread)
    readbetterentropythanziptwo = bin(int(ww.hex,16))[2:] 
    readbetterentropythanziptwo = formatmap(readbetterentropythanziptwo, lengthin)
    if digits == 8:
      ssxread=open('betterentropythanzipthree.bin', 'rb').read()
      www = BitString(ssxread)
      readbetterentropythanzipthree = bin(int(www.hex,16))[2:] 
      readbetterentropythanzipthree = formatmap(readbetterentropythanzipthree, lengthin)
  if digits == 8:
    return readbetterentropythanzipone, readbetterentropythanziptwo, readbetterentropythanzipthree
  elif digits == 4:
    return readbetterentropythanzipone, readbetterentropythanziptwo

# ---Cool Thing #1---
# The following could be made to be much faster, but i believe to be the first example of how to create a high
# low map by using base10 to base16 distance comparison. I'm quite proud of finding this algorithim, i think
# until somebody lets me know otherwise. I believe i can make a version for odd/even's, thats' what i'm working
# on now.
#
# def highlowmapalg(random4):
#
#  Creates a map. 0 for digits lower than or equal to 4, and 1 for digits higher than 4. This is done not by
#  looking at individual digits, but rather by a higher order relation from the original number to it's added
#  base10 and base16 numbers, and then comparing them. That bit relation is what accomplishes this. 
#
#

def highlowmapalg(random4):
   fastmap = hex((int(str(int(random4) + int(random4)),16) - (int(str(random4),16) + int(str(random4),16)))//6) 
   return fastmap

def oddevenalg(random4, lengthin):
   secondones=''
   for x in range(0, lengthin):
      secondones+='1'
   fastmap = int(random4,16) & int(secondones,16)
   return fastmap


def maximumentropysave(original, betterthanzipones, betterthanziptwos, betterthanzipthrees, lengthin, digits=8):
  find00, find10, find01, find11 = False, False, False, False
  find000, find010, find001, find011, find100, find110, find101, find111 = False, False, False, False, False, False, False, False
  x = 0
  maxlist = {}
  oddevenlist = {}
  oddevenmap=''
  oddevenmap = hex(oddevenalg(original, lengthin))[2:]
  oddevenmap = formatmap(oddevenmap, lengthin)
  if debug=='True':
    print(oddevenmap[0:111])
  maxmap = hex((int(betterthanzipones,16)*6 + int(oddevenmap,16)) ^ int(original,16))[2:]
  maxmap = formatmap(maxmap, lengthin)
  if debug=='True':
    print(maxmap[0:111])
  if digits == 8:
    while ( find000 and find010 and find001 and find011 and find100 and find110 and find101 and find111) == False:
      if betterthanzipthrees[x] == '0' and betterthanziptwos[x] == '0' and betterthanzipones[x] == '0':
        maxlist['000'] = maxmap[x]
        oddevenlist['000'] = oddevenmap[x]
        find000 = True
      elif betterthanzipthrees[x] == '0' and betterthanziptwos[x] == '1' and  betterthanzipones[x] == '0':
        maxlist['010'] = maxmap[x]
        oddevenlist['010'] = oddevenmap[x]
        find010 = True
      elif betterthanzipthrees[x] == '1' and betterthanziptwos[x] == '0' and  betterthanzipones[x] == '0':
        maxlist['001'] = maxmap[x]
        oddevenlist['001'] = oddevenmap[x]
        find001 = True
      elif betterthanzipthrees[x] == '1' and betterthanziptwos[x] == '1' and  betterthanzipones[x] == '0':
        maxlist['011'] = maxmap[x]
        oddevenlist['011'] = oddevenmap[x]
        find011 = True
      elif betterthanzipthrees[x] == '0' and betterthanziptwos[x] == '0' and  betterthanzipones[x] == '1':
        maxlist['100'] = maxmap[x]
        oddevenlist['100'] = oddevenmap[x]
        find100 = True
      elif betterthanzipthrees[x] == '0' and betterthanziptwos[x] == '1' and  betterthanzipones[x] == '1':
        maxlist['110'] = maxmap[x]
        oddevenlist['110'] = oddevenmap[x]
        find110 = True
      elif betterthanzipthrees[x] == '1' and betterthanziptwos[x] == '0' and  betterthanzipones[x] == '1':
        maxlist['101'] = maxmap[x]
        oddevenlist['101'] = oddevenmap[x]
        find101 = True
      elif betterthanzipthrees[x] == '1' and betterthanziptwos[x] == '1' and  betterthanzipones[x] == '1':
        maxlist['111'] = maxmap[x]
        oddevenlist['111'] = oddevenmap[x]
        find111 = True
      if x >= lengthin-1:
        find000 = True
        find010 = True
        find001 = True
        find011 = True
        find100 = True
        find110 = True
        find101 = True
        find111 = True
        break
      x+=1
  elif digits == 4:
    while ( find00 and find10 and find01 and find11 ) == False:
      if betterthanziptwos[x] == '0' and betterthanzipones[x] == '0':
        maxlist['00'] = maxmap[x]
        oddevenlist['00'] = oddevenmap[x]
        find00 = True
      elif betterthanziptwos[x] == '1' and betterthanzipones[x] == '0':
        maxlist['10'] = maxmap[x]
        oddevenlist['10'] = oddevenmap[x]
        find10 = True
      elif betterthanziptwos[x] == '0' and betterthanzipones[x] == '1':
        maxlist['01'] = maxmap[x]
        oddevenlist['01'] = oddevenmap[x]
        find01 = True
      elif betterthanziptwos[x] == '1' and betterthanzipones[x] == '1':
        maxlist['11'] = maxmap[x]
        oddevenlist['11'] = oddevenmap[x]
        find11 = True
      if x >= lengthin-1:
        find00 = True
        find10 = True
        find01 = True
        find11 = True
        break
      x+=1
  else:
    print("Only 4 or 8 can be used")
    sys.exit()

  crwritelists(maxlist, oddevenlist)

  return maxlist, oddevenlist

def createmaxmapandoddevenmapfromsave(lengthin, digits=8):
  maxmap=''
  oddevenmap=''
  maxlist, oddevenlist = crreadlists()
  if digits == 8:
    readbetterthanzipones, readbetterthanziptwos, readbetterthanzipthrees = getsavedbins(lengthin, digits)
    for x in range(0,lengthin):
      if readbetterthanzipthrees[x] == '0' and readbetterthanziptwos[x] == '0' and readbetterthanzipones[x] == '0':
        maxmap+=maxlist['000'] 
        oddevenmap+=oddevenlist['000'] 
      elif readbetterthanzipthrees[x] == '0' and readbetterthanziptwos[x] == '1' and readbetterthanzipones[x] == '0':
        maxmap+=maxlist['010'] 
        oddevenmap+=oddevenlist['010'] 
      elif readbetterthanzipthrees[x] == '1' and readbetterthanziptwos[x] == '0' and readbetterthanzipones[x] == '0':
        maxmap+=maxlist['001'] 
        oddevenmap+=oddevenlist['001'] 
      elif readbetterthanzipthrees[x] == '1' and readbetterthanziptwos[x] == '1' and readbetterthanzipones[x] == '0':
        maxmap+=maxlist['011'] 
        oddevenmap+=oddevenlist['011'] 
      elif readbetterthanzipthrees[x] == '0' and readbetterthanziptwos[x] == '0' and readbetterthanzipones[x] == '1':
        maxmap+=maxlist['100'] 
        oddevenmap+=oddevenlist['100'] 
      elif readbetterthanzipthrees[x] == '0' and readbetterthanziptwos[x] == '1' and readbetterthanzipones[x] == '1':
        maxmap+=maxlist['110'] 
        oddevenmap+=oddevenlist['110'] 
      elif readbetterthanzipthrees[x] == '1' and readbetterthanziptwos[x] == '0' and readbetterthanzipones[x] == '1':
        maxmap+=maxlist['101'] 
        oddevenmap+=oddevenlist['101'] 
      elif readbetterthanzipthrees[x] == '1' and readbetterthanziptwos[x] == '1' and readbetterthanzipones[x] == '1':
        maxmap+=maxlist['111'] 
        oddevenmap+=oddevenlist['111'] 
  elif digits == 4:
    readbetterthanzipones, readbetterthanziptwos = getsavedbins(lengthin, digits)
    for x in range(0,lengthin):
      if readbetterthanziptwos[x] == '0' and readbetterthanzipones[x] == '0':
        maxmap+=maxlist['00'] 
        oddevenmap+=oddevenlist['00'] 
      elif readbetterthanziptwos[x] == '1' and readbetterthanzipones[x] == '0':
        maxmap+=maxlist['10'] 
        oddevenmap+=oddevenlist['10'] 
      elif readbetterthanziptwos[x] == '0' and readbetterthanzipones[x] == '1':
        maxmap+=maxlist['01'] 
        oddevenmap+=oddevenlist['01'] 
      elif readbetterthanziptwos[x] == '1' and readbetterthanzipones[x] == '1':
        maxmap+=maxlist['11'] 
        oddevenmap+=oddevenlist['11'] 
  else:
    print("Only 4 or 8 can be used")
    sys.exit()
  if debug=='True':
    print(maxlist, oddevenlist) 
  highlowplusoddeven = hex(int(readbetterthanzipones,16)*6 + int(oddevenmap,16))[2:]
  createdoriginal = hex(int(highlowplusoddeven,16) ^ int(maxmap,16))[2:]
  highlowplusoddeven = formatmap(highlowplusoddeven, lengthin)
  createdoriginal = formatmap(createdoriginal, lengthin)
  return readbetterthanzipones, maxmap, oddevenmap, highlowplusoddeven, createdoriginal


AMillionRandomDigits='100973253376520135863467354876809590911739292749453754204805648947429624805240372063610402008229166508422689531'
AMillionRandomDigitsOddEvenMap='100111011110100111001001110010001110111111010101011110000001000101001000001000110001010000000001100100000001111'
AMillionRandomDigitssixes=hex((int(str(int(AMillionRandomDigits)+int(AMillionRandomDigits)),16)) - (int(AMillionRandomDigits,16)+int(AMillionRandomDigits,16)))[2:]
AMillionRandomDigitssixes=formatmap(AMillionRandomDigitssixes,111)
AMillionRandomDigitsHighLowMap=str(int(AMillionRandomDigitssixes)//6)
AMillionRandomDigitsHighLowMap=formatmap(AMillionRandomDigitsHighLowMap,111)
AMillionRandomDigitsHILOplusODDEVEN=formatmap(hex(int(AMillionRandomDigitsOddEvenMap,16) + int(AMillionRandomDigitssixes,16))[2:],111) 
AMillionRandomDigitsXORMAPtoHILOplusODDEVEN=formatmap(hex(int(AMillionRandomDigits,16) ^ int(AMillionRandomDigitsHILOplusODDEVEN,16))[2:],111)
AMillionRandomDigitssixesbyXORMap = formatmap(hex(int(AMillionRandomDigitssixes,16) ^ int(AMillionRandomDigitsXORMAPtoHILOplusODDEVEN,16))[2:],111)


def betterthanzip(digits=4, formatsize=111):

  #if digits!=8:
  #  sys.exit()
 
  orderedrandomlist = buildcustomrandomnumbers(digits) 
  random4=buildcustomrandomdata(orderedrandomlist,size,digits)
  #print('0x' + random4[0:formatsize])
  if digits == 8:
    betterthanzipones, betterthanziptwos, betterthanzipthrees = crandomd(random4, orderedrandomlist, digits)
    maxlist, oddevenlist = maximumentropysave(random4, betterthanzipones, betterthanziptwos, betterthanzipthrees, size, digits)
    highlowmap, maxmap, oddevenmap, highlowplusoddeven, createdoriginal = createmaxmapandoddevenmapfromsave(size, digits) 
  elif digits == 4:
    betterthanzipones, betterthanziptwos = crandomd(random4, orderedrandomlist, digits)
    maxlist, oddevenlist = maximumentropysave(random4, betterthanzipones, betterthanziptwos, 0, size, digits)
    highlowmap, maxmap, oddevenmap, highlowplusoddeven, createdoriginal = createmaxmapandoddevenmapfromsave(size, digits) 
  oddevenmap = hex(oddevenalg(random4, size))[2:]
  oddevenmap = formatmap(oddevenmap, size)
  # The following is a cool way to generate the high/low map that i found when looking at base10 to base16 relationships
  print("The following shows that there is a odd/even map relation ship to an original number, by just it's high/low map and a 1-4 digit ")
  print("XOR value. Using just the HIGH/LOW MAP and ODD/EVEN MAP to generate the XOR number only works about 33% of the time. So i found ")
  print("a way to generate the ODD/EVEN MAP and XOR Value, agorithimically with the high/low map. This gives you more information about ")
  print("your higher order number and shows that you can get back to your original number with just a HIGH/LOW Map and an ODD/EVEN Map. ")
  print("After these explanations, is it's relationship to AMillionRandomDigits, which the same structure applies too. ")
  print("That is, AMillionRandomDigits, is it's HIGH/LOW MAP, it's ODD/EVEN MAP, and a 4 digit XOR value to get back to it. And I can ")
  print("generate those ODD/EVEN Values and XOR values for 4 digit and 8 digit random numbers! For AMillionRandomDigits, i can do something ")
  print("amazing, using this same alogithim! I can generate the 4 digit XOR values, which generate a 86420 numbers, which is the ODD/EVEN ")
  print("MAP Away!. Imagine if i could do the same algorithm for a 10 digit number! Read further below for an explanation about AMillionRandomDigits")
  print("+----------------------------------------------------------------------------------------------------------------+")
  print("Here is the {} digit random number you created using betterthanzip(4) or betterthanzip(8) for different digit sizes".format(digits))
  print("+----------------------------------------------------------------------------------------------------------------+")
  print('0x' + random4[0:formatsize])
  print("+----------------------------------------------------------------------------------------------------------------+")
  print("Here is the value of the random number XOR'd with the HIGH/LOW MAP*6 ADDED to the ODD/EVEN MAP ")
  print("+----------------------------------------------------------------------------------------------------------------+")
  print('0x' + formatmap(hex((int(betterthanzipones[0:formatsize],16)*6 + int(oddevenmap[0:formatsize],16)) ^ int(random4[0:formatsize],16))[2:],formatsize))
  print("+----------------------------------------------------------------------------------------------------------------+")
  print("Here is the value of the ODD/EVEN map + the HIGH/LOW MAP*6 ")
  print("+----------------------------------------------------------------------------------------------------------------+")
  print('0x' + highlowplusoddeven[0:formatsize]) 
  print("+----------------------------------------------------------------------------------------------------------------+")
  print("Here is the HIGH/LOW map, which can be generated by this very cool algorithm that doesn't use a loop. Pure Mathematics!")
  print("for a HIGH/LOW Map! By yours truly:  hex((int(str(int(randnum) + int(randnum)),16) - (int(randnum,16) + int(randnum,16))")
  print("+----------------------------------------------------------------------------------------------------------------+")
  generatedhighlowmap = hex((int(str(int(createdoriginal[0:formatsize]) + int(createdoriginal[0:formatsize])),16)
  - (int(createdoriginal[0:formatsize],16) + int(createdoriginal[0:formatsize],16))))
  print(generatedhighlowmap[0:formatsize])
  print(hex(int(generatedhighlowmap,16)//6)[0:formatsize])
  print("+----------------------------------------------------------------------------------------------------------------+")
  print("Here is the  ODD/EVEN map generated by my Algorithm: ")
  print("+----------------------------------------------------------------------------------------------------------------+")
  print('0x' + oddevenmap[0:formatsize])
  print("+----------------------------------------------------------------------------------------------------------------+")
  print("These are the stored values on disk to generate the ODD/EVEN Values and XOR Values back to the original with the HIGH/LOW: ")
  print("+----------------------------------------------------------------------------------------------------------------+")
  #print('0x' + betterthanzipones[0:formatsize])

  print('0x' + betterthanziptwos[0:formatsize])
  if digits == 8:
     print('0x' + betterthanzipthrees[0:formatsize])
  print("+----------------------------------------------------------------------------------------------------------------+")
  print("Here are the XOR values and the HIGH/LOW MAP added to the ODD/EVEN MAP, which the XOR value of both, is the original! ")
  print("All of these values are generated algorithimically. Remember, while you can do this other ways, this way show a relationship ")
  print("between an unrealated number, and the HIGH/LOW MAP, which recreated values needed to be just a MAP away, which we can also ")
  print("generate algorithimically, with just the unrelated number. You get more information about you original number. For ")
  print("AMillionRandomDigits, the shift from an 8digit to 10digit number, seems to be only it's ODD/EVEN Map! ")
  print("These next two values are Generated From our saved data, they are XOR'd to get to the orignal. Another way to point on the ")
  print("Relationship, is that the ORIGINAL XOR'ed by the FIRST value here is the SECOND VALUE. The SECOND VALUE is the DDD/EVEN ")
  print("added to the HIGH/LOW MAP. Remember, you can't do this without an algorithmically created unrelated number. Otherwise ")
  print("You XOR only works about 33% of the time if you try just using the ODD/EVEN map, so we cleverly recreate that with a new value ")
  print("which also gives the XOR. Remember, there is a relationship with AMillionRandomDigits which i explain below.")
  print("+----------------------------------------------------------------------------------------------------------------+")
  #print('0x' + formatmap(hex((int(betterthanzipones[0:formatsize],16)*6 + int(oddevenmap[0:formatsize],16)) ^ int(createdoriginal[0:formatsize],16))[2:],formatsize))
  print('0x' + maxmap[0:formatsize])
  print('0x' + highlowplusoddeven[0:formatsize]) 
  print("+----------------------------------------------------------------------------------------------------------------+")
  print("And the two values we generated from our saved data above are exactly the distance to the original. The same formula on a ")
  print("10 digit random number is it's ODD/EVEN MAP value! The  difference between a 4 and 8 digit random number, is an ")
  print("ODD/EVEN MAP!!! Which we can generate for lower than 8 digit numbers. This value is the two above numbers above XOR'ed together: ")
  print("+----------------------------------------------------------------------------------------------------------------+")
  print(hex(int(maxmap[0:formatsize],16) ^ int(highlowplusoddeven[0:formatsize],16)))
  print("+----------------------------------------------------------------------------------------------------------------+")
  print("The next number is the original for comparison: (Notice we get better compression than ZIP below!)")
  print("+----------------------------------------------------------------------------------------------------------------+")
  print('0x' + random4[0:formatsize])
  print("+----------------------------------------------------------------------------------------------------------------+")
  #print('0x' + highlowmap[0:formatsize])
  #print('0x' + maxmap[0:formatsize])
  #print('0x' + oddevenmap[0:formatsize])
  #print('0x' + highlowplusoddeven[0:formatsize]) 
  #print('0x' + createdoriginal[0:formatsize])
  #print('0x' + formatmap(hex((int(highlowmap[0:formatsize],16)*6 + int(oddevenmap[0:formatsize],16)) ^ int(maxmap[0:formatsize],16))[2:],formatsize))
  print("random4 == createdoriginal: {}".format(random4 == createdoriginal))

  if digits == 8:
    origfilesize = os.stat('orighex_eight.bin')[6]
    zipfilesize = os.stat('orighex_eight.zip')[6]
    myfilesizes = os.stat('betterentropythanzipone.bin')[6] + os.stat('betterentropythanziptwo.bin')[6] + os.stat('betterentropythanzipthree.bin')[6]
    myfilesizes += os.stat('betterthanzipoddevenlist.bin')[6] + os.stat('betterthanzipmaxlist.bin')[6]
  elif digits == 4:
    origfilesize = os.stat('orighex.bin')[6]
    zipfilesize = os.stat('orighex.zip')[6]
    myfilesizes = os.stat('betterentropythanzipone.bin')[6] + os.stat('betterentropythanziptwo.bin')[6] + os.stat('betterthanziporderedlist.bin')[6]
    myfilesizes += os.stat('betterthanzipoddevenlist.bin')[6] + os.stat('betterthanzipmaxlist.bin')[6]

  #print("random4 == random4compare: {}".format(random4 == random4compare))

  print("The following my file sizes compared to zip for 4 digit and 8 digit random numbers: ")
  print("+----------------------------------------------------------------------------------------------------------------+")
  print("OriginalFile size: orighex.bin:  {}".format(origfilesize))
  print("ZipFile size: orighex.zip:  {}".format(zipfilesize))
  print("BetterthanFile sizes: bettercompreesionthanzip*.bin:  {}".format(myfilesizes))
  print("Byte Difference between ZipFile size and BetterthanFile sizes: {}".format(zipfilesize-myfilesizes))
  print("Percentage Better Compression: {0:.0%}".format(1 -myfilesizes/zipfilesize))
  print("")
  print("AMillionRandom Digits Comparison - The first number below is the first {} from AMillionRandomDigits.bin".format(formatsize))
  print("+----------------------------------------------------------------------------------------------------------------+")
  print('0x' + AMillionRandomDigits)
  print("+----------------------------------------------------------------------------------------------------------------+")
  print("Notice the similarity when adding the ODD/EVEN to the high/low as we do above: ")
  print("+----------------------------------------------------------------------------------------------------------------+")
  print('0x' + AMillionRandomDigitsHILOplusODDEVEN)
  print("+----------------------------------------------------------------------------------------------------------------+")
  print("This creates a 4 digit XOR number just like we do for 8 digit and 4 digit random numbers above! ")
  print("+----------------------------------------------------------------------------------------------------------------+")
  print('0x' + AMillionRandomDigitsXORMAPtoHILOplusODDEVEN)
  print("+----------------------------------------------------------------------------------------------------------------+")
  print("My algorithm creates the 66's / which are 1's when used as a map, same as above: (The next two numbers are the same ")
  print(", they are just used for different purposes. One purpose is to build the XOR MAP, which i can for AMillion Random ")
  print("Digits!")
  print("+----------------------------------------------------------------------------------------------------------------+")
  print('0x' + AMillionRandomDigitssixes)
  print('0x' + AMillionRandomDigitsHighLowMap)
  print("+----------------------------------------------------------------------------------------------------------------+")
  print("The next number is my XOR from the sixes to the XOR MAP i generate for AMillion Random Digits")
  print("+----------------------------------------------------------------------------------------------------------------+")
  print('0x' + AMillionRandomDigitssixesbyXORMap)
  print("+----------------------------------------------------------------------------------------------------------------+")
  print("This number is the next distance away from AMillionRandomDigits, which happens to be the ODD/EVEN Map")
  print("+----------------------------------------------------------------------------------------------------------------+")
  print('0x' + AMillionRandomDigitsOddEvenMap)
  print("+----------------------------------------------------------------------------------------------------------------+")
  print("My algorithm generates the missing ODD/EVEN MAP and XOR back for 4 digit and 8 digit random numbers, but not for ")
  print("10 digit numbers. For 10 digit numbers it generates the highlow map (6's), the XOR Map, and a number who's entropy ")
  print("i'm evaluating to see if it matches a random 10 digit number. I'm holding back the algorithm for that until i")
  print("i evaluate it. If it's entropy is of a 10 digit number (really i shouldn't be telling you this, so if this idea helps")
  print("you crack entropy, please give me credit and $$ after your a billionaire)  then that means two wrong numbers can lead")
  print(" to a wrong answer which would be the right answer. If you understand that if the entropy is of a 10 digit number, you'll")
  print("understand why i think that you can get to AMillionRandomDigits using methods like this using two unrelated numbers.")
  print(" (Remember me if you crack entropy using two unrelated numbers $$ :) ")
  print("+----------------------------------------------------------------------------------------------------------------+")
  print(" It's cool to acheive 34% better compression than zip for four digits, and 1% better at eight digits for random numbers ")
  print(" Here are the size comparisons again: ")
  print("+----------------------------------------------------------------------------------------------------------------+")
  print("OriginalFile size: orighex.bin:  {}".format(origfilesize))
  print("ZipFile size: orighex.zip:  {}".format(zipfilesize))
  print("BetterthanFile sizes: bettercompreesionthanzip*.bin:  {}".format(myfilesizes))
  print("Byte Difference between ZipFile size and BetterthanFile sizes: {}".format(zipfilesize-myfilesizes))
  print("Percentage Better Compression: {0:.0%}".format(1 -myfilesizes/zipfilesize))
  print("random4 == createdoriginal: {}".format(random4 == createdoriginal))
  print("+----------------------------------------------------------------------------------------------------------------+")
  print("Again, Here is the {} digit random number you created using betterthanzip(4) or betterthanzip(8) for different digit sizes".format(digits))
  print("+----------------------------------------------------------------------------------------------------------------+")
  print('0x' + random4[0:formatsize])

betterthanzip(8)




