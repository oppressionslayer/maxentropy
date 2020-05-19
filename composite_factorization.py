# You can import these by 
# from composite_factorization import *

# Example Uses:
# In [148]: try_factorization_mod_one((1009*101)**8)                                                                                                            
# Out[148]: [101]

# In [151]: find_prime_factor(1009732533765211)                                                                                                                 
# 239 11344301
# The 239 here is the powers number to find the prime so we can use this next example to find it 
# rather quickly:

# In [152]: try_factorization_mod_one((1009732533765211)**239)                                                                                                  
# Out[152]: [11344301]

# Another Example:
# In [323]: try_factorization_mod_one((1009*1013)**2)
# or
# In [325]: try_factorization_mod_one(1022117**2)
# Out[325]: [1009]

# In [156]: find_prime_factor(1022117)
# 2 1009

# No factorization is used, this is a pure mod method to extract primes from a number


# Most factorization techiniques break down numbers into their prime components. I created a method
# that breaks down a number into it's composite factors which can be rebuilt with 
# build_composite_number:

# In [154]: try_factorization_mod((1009732533765211))                                                                                                           
# Out[154]: [1, 1710, 150, 6, 256, 36, 630, 16, 2, 2]

# In [155]: build_composite_number([1, 1710, 150, 6, 256, 36, 630, 16, 2, 2])                                                                                   
# Out[155]: 1009732533765211

# Interstingly, i use no factorization at all to find the prime numbers, just mod operations, which
# is different from other techniques.

def try_factorization_mod(hm):
  vv = []
  num = hm
  cr = pow(num,1,1<<(num).bit_length()-1)
  while num > 1 and cr != 0:
    while cr != 0:
      prevcr = cr
      cr = num%cr     
    vv.append(prevcr)
    num = (num // prevcr) -1
    cr = num%(1<<(num).bit_length()-1)
  vv.append(num)
  return vv

def try_factorization_mod_one(hm):
  vv = []
  num = hm
  cr = pow(num,1,1<<(num).bit_length()-1)
  while cr != 0:
      prevcr = cr
      cr = num%cr     
  vv.append(prevcr)
  num = (num // prevcr) -1
  cr = num%(1<<(num).bit_length()-1)
  return vv

def find_prime_factor(hm): 
   for x in range(1, 1000):  
     c = try_factorization_mod_one((hm)**x)  
     if c[0] != 1:  
        if hm % c[0] == 0 : 
          print(x,c[0])  
          break  

def build_composite_number(hm):
   si = hm[-1]
   for x in range(len(hm)-2, -1, -1):
      si = si * hm[x] + hm[x]
   return si


