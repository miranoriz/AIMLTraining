def add(num1,num2): 
    return num1+num2

def multiply(num1,num2):
    return num1*num2

def avg(num1,num2): 
    return (num1+num2)/2

def sub(num1,num2):
    return num1-num2

def div(num1,num2):
    return num1/num2

print("Welcome to our calculator")

while True:
    print("--------------------------------------------------------------------------------------------")
    print("Select operation \n1.Add \n2.Substract, \n3.Multiplication \n4.Division \n5.Average \n6.Exit")
    op = int(input("Enter your operation choices: "))

    if (op==6):
        print("Exit")
        break

    if (op <=0 or op>6):
        print("Wrong operation choices. Choose 1-6 only")
    
    else:
     fnum = float(input("Enter first number: "))
     snum = float(input("Enter second number: "))

     if (op==1):
        print(f"Result adding {fnum} and {snum} is : ", add(fnum,snum))
    
     elif (op==2):
        print(f"Result minus {fnum} and {snum} is : ", sub(fnum,snum))

     elif (op==3):
        print(f"Result multiplying {fnum} and {snum} is : ", multiply(fnum,snum))

     elif (op==4):
        print(f"Result dividing {fnum} and {snum} is : ", div(fnum,snum))

     elif (op==5):
        print(f"Average {fnum} and {snum} is : ", avg(fnum,snum))
 
 