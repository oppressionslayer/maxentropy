# This decompresses a message that can be repeated via XOR Math from a compressed huffman tree of the XOR Math
# used to create it. You can change repetition to change the number of repetitions of the compressed message 
# as the message is the math of the symbol table. The binary is the compressed symbols of the XOR math required
# by the message.

# The comparison i wanted to show is how well XOR math handles repitition. Standard Huffman trees would compress
# These with a longer binary string, while we can reduce size by using math to reproduce the repetition.

import ast
from heapq import heappush, heappop, heapify
from functools import reduce


s={'1001': ' ', '1011': "'", '11': '+', '10100': ',', '0': '-', '10001': '1', '100000': '2', '10000110': '5', '10101': ':', '10000111': '{', '1000010': '}'}

read_compressed_binary=bin(0x87bc0cf3f66f031fbdfef66f79fbcfdb3ccfc1fb7bdfef786061ec5d661a937819e7ecde063f7bfdecdef3f79fb6799f83f6f7bfdef0eeb30526f36ff30f6060de37ecdefdf818cfdb3cbacc149bfdeff7b378dfb378dfb6783f6cf33eeb31a4d8187b3679e79e7b6fc32eb31a4db7e37ed9e63bacc6936f7bfdeff7bc2eb31a4dfef3f7b6fcf3bacc69379b7f987aeb31a4dfef6df9e2eb31a4daeb3042)[2:]

def decompressHuffmanCode(a, bit):
    return ('', a[1] + s[a[0]+bit[0]]) if (a[0]+bit[0] in s) else (a[0]+bit[0], a[1])

remainder,sym2freq = reduce(decompressHuffmanCode, read_compressed_binary, ('', ''))

sym2freq = ast.literal_eval(sym2freq)

repetition=150

def encode(symb2freq): 
   heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()] 
   heapify(heap) 
   while len(heap) > 1: 
       lo = heappop(heap) 
       hi = heappop(heap) 
       for pair in lo[1:]: 
           pair[1] = '0' + pair[1] 
       for pair in hi[1:]: 
           pair[1] = '1' + pair[1] 
       heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:]) 
   return dict(sorted(heappop(heap)[1:], key=lambda p: (p, len(p[-1]))))

def decodethebetterstuffplusminux(themap):
  j=0
  y=1
  for c in range(0,len(themap)):
     if j < 0:
        if themap[c] == '-':
            j^=y
        else:
            j^=-y
     else:
        if themap[c] == '-':
            j^=-y
        else:
            j^=y
     y<<=1
  answer=((y>>1)-1)-(abs(j)>>1) 
  return answer

read_compressed_binary = '0110010000100001101111001011101000111011011001011111010011'

s=dict((v,k) for k,v in encode(sym2freq).items())

remainder,bytestr = reduce(decompressHuffmanCode, read_compressed_binary, ('', ''))

print(bytes.fromhex(hex(decodethebetterstuffplusminux(bytestr*repetition))[2:]))  

