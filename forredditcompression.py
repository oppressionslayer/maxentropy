def Xplodermath(s):
    temp = s+1
    s = temp * 2 -1
    return s

def getintanddec(hm):
  return hm, hex(hm)

print ("1009732533765251 is prime. I generated the number 4610676285893622652, which ")
print ("using XOR, get's to double the prime number. ")
print ("First column is the number that doubles over and over until you get to double ")
print ("the prime number when XORED with the 1st Column")
print ("The number we are trying to get to is 2019465067530502, which is double the prime ")
print ("number of 1009732533765251")
print ("")
print ("")
print ("XOR each number in the 2nd column, with the number below. Also do the same with ")
print ("The third column. Example from 3rd column: 6^262 is 256, which is in the first columm ")
print ("If you follow this pattern all the way down you will get to double the prime number ")
print ("")
print ("")
print ("1st Column    2nd 3rd 4th")

# 1009732533765251 is prime. I generated 4610676285893622652 to get to the prime using double
# 128, which is 2**7, all the way down to 1125899906842624, which is 2**50, or 

prime=4610676285893622652
j=63 # Xploder(127) 
for x in range(0,44):
   print(getintanddec(Xplodermath(j)+1), prime-(Xplodermath(j)^prime), Xplodermath(j)- (prime-(Xplodermath(j)^prime)), prime)
   j=Xploder(j)
