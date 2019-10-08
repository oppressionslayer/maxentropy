# To use, just do the following:
# from devilsnum import *
# usage: creategodsanswerfromdevilsnum(1009)
# or creategodsanswerfromdevilsnum(1009, 187)
# or to skip y's by a factor:
# creategodsanswerfromdevilsnum(1009, 187, 2)

def Xploderiter(s, iter=1):
  for x in range(0,iter):
    temp = s+1
    s = temp * 2 -1
  return s

def createdevilsnumSHIFT(hm):
  if hm % 2==0:
    return "This works with odd numbers only right now"
  y=1 
  j=hm
  loopbreak = j + 1
  iterx=2
  while y<loopbreak: 
    y=(1<<iterx)-1 
    iterx+=1
  iterx+=11
  return ((1<<iterx)-1)^j

def creategodsanswerfromdevilsnum(j, y=0, yd=1):
  doublin=0
  prevdoublin=0
  godsnum=0
  godsanswer=0
  firstrun=True
  iterx=0
  origj=j
  j = createdevilsnumSHIFT(j)
  if j == "This works with odd numbers only right now":
    return "This works with odd numbers only right now"
  for x in range(0,1): 
    print("")
    print("USAGE: creategodsanswerfromdevilsnum(yournumber, y, yd)")
    print("y=the number you double by")
    print("yd=the number of times you double y per iterations")
    print("Devils Number: The number generated to get all the results you see. Your number is not used ")
    print(" instead, J=Devils Number, which is then used to calculate all results, leading to your number")
    print("Remember, all results are calculated with the devils number, and it gets to your number with ")
    print("different most values you use as Y, not just powers of 2!")
    print("")
    print("Many times the 3rd column will always give you your original number for different y and yd\'s")
    print("This doesn't work everytime, but you'll notice it works a lot, your number will be in 3rd column")
    print("")
    print("1st Column: iterx")
    print("2nd Column: y=Xploderiter(y,yd) # Meaning you could div//2 yd times to the previous answer")
    print("3rd Column: j-(((y*2)+1)^j)")
    print("4th Column: (((abs(j-(y*2^j)))^((y*2)+1))+2)//2")
    print("5th Column: j-(((y*2)+1)^j)^previous(j-(((y*2)+1)^j))")
    print("")
    print("Your Number: {}".format(origj))
    print("Your Numbers Xploderiter: {}".format(origj*2+1))
    print("Your Devils Numbers: {}, {}".format(j, j+1))
    print("")
    print(iterx, (y*2)+1,doublin, (((abs(j-(y*2^j)))^((y*2)+1))+2)//2, doublin^prevdoublin, )  
    iterx+=1
    while y<j+1: 
       prevdoublin = doublin
       for x in range(0,yd):
         y=(y<<1)+1 
       doublin = j-(((y*2)+1)^j)
       print(iterx, (y*2)+1,doublin, (((abs(j-(y*2^j)))^((y*2)+1))+2)//2, doublin^prevdoublin, )  
       iterx+=1
    godsnum=Xploderiter(y)^j
    godsanswer=abs(j-(((y*2)+1)^j))
  print("")
  print("Your Number: {}".format(origj))
  print("Your Numbers Xploderiter: {}".format(origj*2+1))
  print("Your Devils Numbers: {}, {}".format(j, j+1))
  print("")
  #return len(bin(j)[2:]), j, origj 
