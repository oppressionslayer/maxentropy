# Decompresses the number 1009732533765201 using Huffman

s={'11': '++--', '01': '-+-+-', '000': '+-++++++', '001': '--', '100': '--+-', '101': '----++-+--'}


def decodepattern(pattern, j=1):
   x=2
   for c in range(len(pattern)):
     if pattern[c]=='+':
       j^=x
     else:
       j^=-x
     x<<=1
   return abs(j)

match = True
stream = 0
match = False
peek=''
peekstart=0
peekend=1
sptrint=0b110011111000011010110011
sptrbuff=''
sptr = sptrbuff + bin(sptrint)[2:]
sptrlen = len(sptr)
bytestr=b''
while peekstart+peekend <= sptrlen:
  match=False
  while match == False:
    peek = sptr[peekstart:peekstart+peekend] 
    findptr = s.get(peek)
    while findptr == None:
       peek = sptr[peekstart:peekstart+peekend+stream]
       stream=stream+1
       findptr = s.get(peek)
    if stream == 0:
      peekstart=peekstart+peekend+stream
    else:
      peekstart=peekstart+peekend+stream-1
    stream=0
    bytestr+=s.get(peek).encode()
    match = True
print("Bin length of 1009732533765201 is 50 which is the same as the pattern length")
print("Original Bin of 1009732533765201 is: ")
print(bin(1009732533765201)[2:])
print("Original Pattern:")
print(bytestr)
print("Compressed to: ", bin(13600435)[2:])
print("110011111000011010110011 uncompressed to: ")
print("")
print(decodepattern(bytestr.decode()))
