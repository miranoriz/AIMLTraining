#Module = single python file containing python code

#------square root-----

# import math
# mynum = int(input("Enter number to find out square root: "))
# print(f"Square root of {mynum} is ", math.sqrt(mynum))
# print(f"Square root of {num} is ", round(math.sqrt(num),2)) #<--- get 2 decimal number

#------random number-----

import random
def winner():
 name = input("Enter your name: ")
 luckynum = random.randint(1,10)

 if(luckynum == 1):
  print(f"Congrats {name}! Your cuppon number is {luckynum}. You won the Proton x50")
 else: 
  print(f"Your cuppon number is {luckynum}. Better luck next time {name}")

#------check function inside modules------

# import math
# import inspect
# functions = inspect.getmembers(math, inspect.isbuiltin)
# for n, f in functions: #<----- key,value. nak key sahaja
#     print(n)

#------check sincostan------

# import math
# print(math.sin(45))
# print(math.cos(45))
# print(math.tan(45))

#------date and time------

# import datetime
# import inspect

# print("Today is (date)", datetime.date.today())
# print("Today is (date & time)", datetime.datetime.now())
#formatdate = datetime.datetime.now().strftime('%B %D, %Y') 
# print("Today is (time)", datetime.datetime.now().time())
# formattime = datetime.datetime.now().strftime('%I %M %S %p') #<-- hour minute second am/pm
# print(formattime)

#------os------

# import os

#list directory
# dirs = os.listdir()
# for rdr in dirs:
#     print (rdr)

#current directory
# print(os.getcwd())

# functions = inspect.getmembers(os, inspect.isbuiltin)
# for n, f in functions: #<----- key,value. nak key sahaja
#     print(n)








