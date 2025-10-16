# username = input("Enter your username : ")
# age = int(input("Enter your age : "))
# salary = float(input("Enter your salary : "))
# databaseKn = bool(input("Do you know database? : "))

# print("Welcome Mrs ", username)
# print("Your age is ", age)
# print("Your salary is ", salary)
# print("Know the database ", databaseKn)

# ----------------addition----------------
# num1 = int(input("Enter First Number : "))
# num2 = int(input("Enter Second Number : "))
# Result = num1 + num2
# print(f"The result of addition of {num1} and {num2} is {Result}")

# ----------------multiplication----------------
# num1 = int(input("Enter First Number : "))
# num2 = int(input("Enter Second Number : "))
# Result = num1 * num2
# print(f"The result of multiplication of {num1} and {num2} is {Result}")

#----------------division----------------
# num1 = int(input("Enter First Number : "))
# num2 = int(input("Enter Second Number : "))
# Result = num1 / num2
# print(f"The result of division of {num1} and {num2} is {Result}")

#----------------finding remainder----------------
# num1 = int(input("Enter First Number : "))
# num2 = int(input("Enter Second Number : "))
# Result = num1 % num2
# print(f"The Remainder of division of {num1} and {num2} is {Result}")

#----------------taking multiple input----------------
num1,num2 = input("Enter two number separated by space ").split()
result = int(num1) + int(num2)
print(f"The addition of numbers that you entered are {num1} and {num2} is {result}")
