# use python3 not python2
# Compress repetition

from bitstring import BitString
import gzip

def compressnumberpatter(filename, hm, buf=0,hexbuf=0):
  zzread=open(filename, 'rb').read()
  zzhex=zzread.hex()
  while zzhex[hexbuf] == '0':
     hexbuf+=1
  hm = seethis(int(zzread.hex(),16))
  compress = (int(''.join(hm),2)).to_bytes(((int(''.join(hm),2)).bit_length()+7)//8,'big')   
  zz = open(filename + '.lars.bin', 'wb')
  BitString('0x' + gzip.compress(compress).hex()).tofile(zz)
  zz.close()
  while hm[buf] == '0':
    buf+=1
  if buf == 0:
    buf = ''
  if hexbuf == 0:
    hexbuf = ''
  writestring = str(buf) + ',' + str(hexbuf)
  with open(filename + '.lars.bin.pickle', 'w') as HI:
    HI.write(writestring)


def uncompressnumberpatter(filename, output, zeros='', hexzeros=''):
   with open(filename + '.pickle', 'r') as HI:
     buf, hexbuf = HI.read().split(',')
   if buf == '':
      buf = '0'
   if hexbuf == '':
      hexbuf = '0'
   for c in range (0, int(buf,10)):
     zeros += '0'
   for c in range (0, int(hexbuf,10)):
     hexzeros += '0'
   zzread = open(filename, 'rb').read()
   uncompress = gzip.decompress(zzread)
   strunc = zeros + bin(int(uncompress.hex(),16))[2:]
   j = seethat(strunc)
   j = '0x' + hexzeros + hex(j)[2:]
   zz = open(output, 'wb')
   BitString(j).tofile(zz)
   zz.close()

def seethis(hm):
  j=hm
  stringplusminus=''
  while j != 1:
    if j>>1 == j-(j>>1):
      stringplusminus = '0' + stringplusminus 
    else:
      stringplusminus = '1' + stringplusminus
    j-=(j>>1)
  return stringplusminus

def seethat(hm):
  j=1
  for c in range(0, len(hm)):
    if hm[c] == '0':
      j<<=1
    else:
      j = (j<<1)-1
  return j
