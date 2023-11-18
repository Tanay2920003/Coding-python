from time import sleep


import random
def toss():
         print("Tossing COIN ...")
         sleep(2)
         d=random.choice(c)
         if d==1:
             print("Heads")
         else:
             print("tails")
         
         
         

c=[0,1]
d=1
a=input("Toss coin (Y/N)?")
while (a=="Y"or "y"):
    toss()
    a=input("again Y/N ?")
    if a=="N"or "n":
        break
    else:
        continue
        
