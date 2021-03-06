# To use, just do the following:
# from devilsnum import *
# usage: creategodsanswerfromdevilsnum(1009)
# or creategodsanswerfromdevilsnum(1009, 187)
# or to skip y's by a factor:
# creategodsanswerfromdevilsnum(1009, 187, 2)

def Xploderiter(s, iter=1):
  temp = s+1
  s = (temp << (iter))-1
  return s

def createdevilsnumBITLENGTH(hm):
 return (1<<hm.bit_length()<<12)-1^hm

def creategodsanswerfromdevilsnum(j, y=0, yd=1, usedevilsnum='yes'):
  doublin=0
  prevdoublin=0
  godsnum=0
  godsanswer=0
  firstrun=True
  iterx=0
  origj=j
  even=False
  if j % 2 == 0:
     even=True
  if usedevilsnum == 'yes':
    j = createdevilsnumBITLENGTH(j)
  if j == "This works with odd numbers only right now":
    return "This works with odd numbers only right now"
  for x in range(0,1): 
    print("")
    print("USAGE: creategodsanswerfromdevilsnum(yournumber, y, yd)")
    print("y=the number you double by")
    print("yd=the number of times you double y per iterations")
    print("Devils Number: The number generated to get all the results you see. Your number is not used ")
    print(" instead, J=Devils Number, which is then used to calculate all results, leading to your number")
    print("")
    print("Many times the 3rd column will always give you your original number for different y and yd\'s")
    print("This doesn't work everytime, but you'll notice it works a lot, your numner will be in 3rd column")
    print("")
    print("J = {} - The Devils number for all operations below".format(j))
    print("1st Column: iterx")
    print("2nd Column: y=Xploderiter(y,yd) # Meaning you could div//2 yd times to the previous answer")
    print("3rd Column: j-(((y*2)+1)^j)")
    if even == False:
      print("4th Column: (((abs(j-(y*2^j)))^((y*2)+1))+2)//2")
    else:
      print("4th Column: (((abs(j-(y*2^j)))^((y*2)+1)))//2")
    print("5th Column: j-(((y*2)+1)^j)^previous(j-(((y*2)+1)^j))")
    print("")
    print("Your Number: {}".format(origj))
    print("Your Numbers Xploderiter: {}".format(origj*2+1))
    if even == False:
      print("Your Devils Number and it's advocate: {}, {}".format(j, j+1))
    else:
      print("Your Devils Number and it's advocate: {}, {}".format(j, j-1))
    print("XOR Columns 2 and 3 to see your numbers Xploderiter") 
    print("")
    if even == False:
       print(iterx, (y*2)+1,doublin, (((abs(j-(y*2^j)))^((y*2)+1))+2)//2, doublin^prevdoublin, )  
    else:
       print(iterx, (y*2)+1,doublin, (((abs(j-(y*2^j)))^((y*2)+1)))//2, doublin^prevdoublin, ) 
    iterx+=1
    while y<j+1: 
       prevdoublin = doublin
       for x in range(0,yd):
         y=(y<<1)+1 
       doublin = j-(((y*2)+1)^j)
       if even == False:
          print(iterx, (y*2)+1,doublin, (((abs(j-(y*2^j)))^((y*2)+1))+2)//2, doublin^prevdoublin, )  
       else:
          print(iterx, (y*2)+1,doublin, (((abs(j-(y*2^j)))^((y*2)+1)))//2, doublin^prevdoublin, )  
       iterx+=1
    godsnum=Xploderiter(y)^j
    godsanswer=abs(j-(((y*2)+1)^j))
  print("")
  print("Your Number: {}".format(origj))
  print("Your Numbers Xploderiter: {}".format(origj*2+1))
  if even == False:
    print("Your Devils Number and it's advocate: {}, {}".format(j, j+1))
  else:
    print("Your Devils Number and it's advocate: {}, {}".format(j, j-1))
  print("XOR Columns 2 and 3 to see your numbers Xploderiter")
  print("")
  #return len(bin(j)[2:]), j, origj 
  print("IF your on repl.it, just copy paste the entry below this message into the window and hit enter/return on your keboard to keep testing different numbers:")
  print("creategodsanswerfromdevilsnum(1009,187)")

creategodsanswerfromdevilsnum(1009)
