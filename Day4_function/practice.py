
#Write a function to find out cube of given number

# def cube(num):
#     #return num*num*num
#     return pow(num,3)

# input = int(input("Enter your number: "))
# print(f"The cube of {input} is: ", cube(input))

#----------------------------------------------------

#Write a function to calculate bonus of given salary
#Function take salary as input and return bonus (10% of salary)

# def bonus(num):
#     return num*0.1

# input = float(input("Enter your salary: RM"))
# print(f"The bonus of salary {input} is: RM", bonus(input))

#---------------------------------------------------

#write a function that convert inches to cms
#1 inc = 2.54 cm

# def convert(num):
#     return num*2.54

# num = int(input("Enter number to convert in inch: "))
# print(f"{num} inch to cm is {convert(num)} cm")


#---------------------------------------------------

#write a function that display name

# def name(name):
#     return name

# name = input("Enter name ")
# print(f"Your name is : ",name(name))

#---------------------------------------------------

#write a function to find out table of given number

def table(num):
 for i in range(1,11):
    print(f"{num}*{i} = {num*i}")
 
number = int(input("Enter a number: "))
print(f"The time table of {number} is:")
table(number)
              
    



