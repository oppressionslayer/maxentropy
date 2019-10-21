# use python3 not python2
# you must install pip install bitstring
# to run

from bitstring import BitString
import gzip

def n():
  global x
  global j
  j = j^-x
  x=x<<1

def p():
  global x 
  global j
  j = j^x
  x=x<<1


def creategodsnumBITLENGTH(hm):
  return (2<<hm.bit_length()-1<<1)-1^hm

def Xploder(s, iter=1):
  temp = s+1
  s = (temp << (iter))-1
  return s

def askthehigherorderforonezeropattern(j=1009):
   y=1
   origj = j
   j = creategodsnumBITLENGTH(j)
   #iterx=1
   strpattern=''
   firsta = ((j-(j^Xploder(y)))>>1)+1
   while ( y//2 < j ) :
      #a =((j-(j^Xploder(y)))//2)+1
      b = (j-(j^Xploder(y)))//2 ^ (j-(j^Xploder(y,2)))//2
      if b > 0:
         pattern='1'
      else:
         pattern='0'
      strpattern+=pattern
      #equation = '{}^{}2**{}'.format(a,pattern,iterx)
      #if prnt == True:
        #print(j^y, j-(j^y), j-(j-y), j^Xploder(y), j-(j^Xploder(y)), a, equation)
      #   print(pattern, equation)
      y=Xploder(y)
      #iterx+=1
   return firsta, strpattern[:-1]


def decompressanyLarsAlg(filename, num, buf=''):
  global x
  global j
  zeros=''
  zzread = open(filename, 'rb').read()
  pattern = buf + bin(int(gzip.decompress(zzread).hex(),16))[2:]
  j = num
  x = 2**1
  for c in range(0, len(pattern)):
     if pattern[c] == '0':
        n()
     else:
        p()
  j = abs(j)
  msg = hex(j)[2:]
  #print(bytes.fromhex(msg).decode())
  zzwrite = open(filename + '.out', 'wb')
  BitString(hex(j)).tofile(zzwrite)
  zzwrite.close()
  return abs(j)


def createpdfLarsAlgbin(filename):
  zzread = open(filename, 'rb').read() 
  e = askthehigherorderforonezeropattern(int(zzread.hex(),16))
  compress = (int(''.join(e[1]),2)).to_bytes(((int(''.join(e[1]),2)).bit_length()+7)//8,'big')   
  zz = open(filename + '.lars.bin', 'wb')
  BitString('0x' + gzip.compress(compress).hex()).tofile(zz)
  zz.close()
  return e[0], e[1][0:10]


def writepdfLarsAlg(filename, output, num, buf):
  global x
  global j
  zeros=''
  zzread = open(filename, 'rb').read()
  for x in range (0, buf):
    zeros += '0'
  pattern =  zeros + bin(int(gzip.decompress(zzread).hex(),16))[2:]
  j = num
  x = 2**1
  for c in range(0, len(pattern)):
     if pattern[c] == '0':
        n()
     else:
        p()
  j = abs(j)
  msg = hex(j)[2:]
  zz = open(output, 'wb')
  BitString(hex(j)).tofile(zz) 
  zz.close()
  #print(bytes.fromhex(msg).decode())
  return abs(j)

createpdfLarsAlgbin('Updated_MyResume_Lars_Rocha.pdf')

# In [8]: createpdfLarsAlgbin('Updated_MyResume_Lars_Rocha.pdf')                                                                                                                 
# Out[8]: (0, '0001110001')


# The 0, is the first 0 returned by createpdfLarsAlgbin. The 3 is the buffer to make the correct bin
# 0001110001 is a bin, but you need to add 3 0's to it, hence the 3 in the call.

writepdfLarsAlg('Updated_MyResume_Lars_Rocha.pdf.lars.bin', 'Updated_MyResume_Lars_Rocha.uncompressed.pdf',0,3) 

createpdfLarsAlgbin('random-org.txt') 

# In [10]: createpdfLarsAlgbin('random-org.txt')                                                                                                                                 
# Out[10]: (0, '0001110110')

# The 0, is the first 0 returned by createpdfLarsAlgbin. The 3 is the buffer to make the correct bin
# 0001110001 is a bin, but you need to add 3 0's to it, hence the 3 in the call.

writepdfLarsAlg('random-org.txt.lars.bin', 'random-org.lars.txt', 0 , 3) 
