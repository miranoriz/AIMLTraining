def display():
    print("welcome")

def welcome(name):
    print("Welcome", name)

def cube(num):
    # num1= num*num*num
    # print(f"The cube of {num} is {num1}")
    return num*num*num


def square(num):
    return num*num

#display()
# welcome('mira')

# username = input("Enter your name: ")
# number = int(input("Enter a number: "))

# print("_______________________________________________\n")
# welcome(username)
# print(f"The cube of {number} is {cube(number)} and the square of {number} is {square(number)}")

#---------------------------------------------

def bonus(salary):
    return salary*0.1

my_sal = float(input("Enter your salary: "))
my_bonus = bonus(my_sal)
print(f"Your salary : {my_sal} and bonus is : {my_bonus}")
print(f"Your salary after bonus is ", my_sal+my_bonus)


