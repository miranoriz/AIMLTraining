#function = a block of resusable code

#resusablitiy = write once, use many time
#modularity = dvide large program into smaller part
#readibility = code is cleaner
#debugging = easier to find error

#------------------------------------------

# def function_name(parameters):
#     statement(s)

#------------------------------------------

#function without parameter

# def welcome():
#     print("welcome to function")
#     print("our first function")

# welcome()

#------------------------------------------

#function with parameter

# def welcome(username):
#     print("Welcome to function Ms", username)

# name = input("Enter your name: ")
# welcome(name)

#------------------------------------------

#function with parameter & return

def add(num1,num2): 
    return num1+num2

def multiply(num1,num2):
    return num1*num2

fnum = int(input("Enter your first number: "))
snum = int(input("Enter your second number: "))

print(f"The result of adding number of {fnum} and {snum} is : " , add(fnum,snum))
print(f"The result of multiplying number {fnum} and {snum} is : " , multiply(fnum,snum))
