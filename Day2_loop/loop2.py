# count = 1
# print("print number from 1 to 100")
# while(count<=100):
#     print(count, end=" ")
#     count +=1

# print("print number from 1 to 100 before we get the numbers divisible by 11")
# count = 1 
# while(count<=100):
#   if(count%11==0):
#     break
#   print(count, end=" ")
#   count +=1

# print("number from 1 to 100 that are not divisible by 11")
# count = 1 
# while(count<=100):

#   if(count%11==0):
#     count +=1
#     continue
#   print(count, end=" ")

#   count +=1

# print("number from 1 to 100 that are divisible by 11")
# count = 1 
# while(count<=100):

#   if(count%11!=0):
#     count +=1
#     continue
#   print(count, end=" ")
#   count +=1

# while loop when we do not know range or the unexpected input, for loop when we know the range 

# for i in range(1,100):
#    if (i%5!=0):
#        i += 10
#        continue 
#    print(i, end=" ")

correctpwd = "mira"

count = 1

while True:
    pwd = input("Enter password : ")
    if (correctpwd==pwd):
       print("Welcome \nGame Started!")
       break
    else:
       print("Wrong password. please try again")
    count +=1
    if(count>3):
     print("Blocked for futher attempted")
     break

  
  

    





