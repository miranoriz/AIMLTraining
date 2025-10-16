#write a function to check the number is odd or even

def check_Even(num):
    if (num%2==0):
        print(f"{num} is Even number")
    else:
        print(f"{num} is Odd number")

number = int(input("Enter a number to check even or odd: "))
check_Even(number)