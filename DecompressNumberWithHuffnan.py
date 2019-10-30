# Uncompresses the number: 1009732533765201
# which has the binary:
# 0b11100101100101100010101100111111100100010001010001
# Our compressed binary is:
# 110011111000011010110011
# We compress a variable length pattern that is decoded 
# to try to acheive nearly as good or better compression 
# than binary compression
# S is a representation of XOR math that is 
# required to rebuild the original number
# so we don't compress the number itself, we compress
# the math to rebuild the number instead

from functools import reduce

s={'11': '++--', '01': '-+-+-', '000': '+-++++++', '001': '--', '100': '--+-', '101': '----++-+--'}
compressed_binary='110011111000011010110011'

def decodepattern(pattern, j=1):
   x=2
   for c in range(len(pattern)):
     if pattern[c]=='+' or pattern[c]=='1':
       j^=x
     else:
       j^=-x
     x<<=1
   return abs(j)

def lefttoright(aggregate, bit):
    prefix, out = aggregate
    key = prefix + bit
    return ('', out + s[key]) if (key in s) else (key, out)

remainder,uncompressed_string = reduce(lefttoright, compressed_binary, ('', ''))
print(uncompressed_string)

answer = decodepattern(uncompressed_string)

print("Bin length of 1009732533765201 is 50 which is the same as the pattern length")
print("Original Bin of 1009732533765201 is: ")
print(bin(1009732533765201)[2:])
print("Original Pattern:")
print(uncompressed_string)
print("Compressed to: ", bin(13600435)[2:])
print("110011111000011010110011 uncompressed to the original string pattern of : ")
print(uncompressed_string)
print("Which then i was able to recreate the original integer of: ")
print(decodepattern(uncompressed_string))
