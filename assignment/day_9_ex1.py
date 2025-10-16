#write a program using function to find greatest of 3 numbers entered by user

def maximum(a,b,c):
   return max(a,b,c)
   
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
print(f'The greatest between {num1},{num2} and {num3} is' , maximum(num1,num2,num3))

