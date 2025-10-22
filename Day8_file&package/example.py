from package import calc

while True:
 try:
    fnum = float(input("Enter first number: "))
    snum = float(input("Enter second number: "))
    op = input("Choose operation +,-,*,/ : \t")

    if(op=='+'):
        print(f"Result of addition of {fnum} and {snum} is ", calc.add(fnum,snum))
    elif(op=='-'):
        print(f"Result of substraction of {fnum} and {snum} is ", calc.sub(fnum,snum))
    elif(op=='*'):
        print(f"Result of addition of {fnum} and {snum} is ", calc.multiply(fnum,snum))
    elif(op=='/'):
        print(f"Result of addition of {fnum} and {snum} is ", calc.div(fnum,snum))
    else: 
        print("Wrong choice")
        raise ValueError

 except ZeroDivisionError as ze:
    print("Divison by 0 is not alllowed",ze)

 except ValueError as ve:
    print("Error in value",ve)

 except Exception as e:
    print("Error",e)

 choice=input("Do you want to continue? if yes press y").lower() #<-- take lower alphabet
 if (choice!='y'):
    print("Bye")
    break

# finally:
#     print("End of program")
