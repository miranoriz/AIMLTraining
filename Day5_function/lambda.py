#lambda = (anonymous) fuction that are small and one line

# add = lambda x, y: x+y
# mul = lambda x, y: x*y
# div = lambda x, y: x/y
# sub = lambda x, y: x-y
# avg = lambda x, y: (x+y)/2

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# # print(add(num1,num2))
# # print(mul(num1,num2))
# # print(div(num1,num2))
# # print(sub(num1,num2))
# # print(avg(num1,num2))

# ----------------------------------------------------

#find out odd and even

check_odd = lambda x : "odd" if x%2==1 else "even"
num1 = int(input("Enter number: "))
print(f"The {num1} is {check_odd(num1)}")



