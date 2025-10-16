#write a program using function to find greatest of 3 numbers entered by user

def maximum(a,b,c):
   return max(a,b,c)

print("\nEnter Three Numbers to find maximum number") 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
print(f'The greatest between {num1},{num2} and {num3} is' , maximum(num1,num2,num3))


#-----------------if user input is in loop-----------------------

def maximum(numbers):
    return max(numbers)

print("\nEnter Three Numbers to find maximum number")

numbers = [] 
for i in range(1, 4): 
    num = int(input(f"Enter your number: "))
    numbers.append(num)

print(f"The greatest number  between {numbers[0]}, {numbers[1]} and {numbers[2]} is:", maximum(numbers))

