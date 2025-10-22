class Account():

    def __init__(a,ac_holder,bal):
        a.ac_holder = ac_holder 
        a.bal = bal

    def deposit(b,amount):
        b.bal += amount 
        print("Balance after deposit is: ", b.bal)

    def withdraw(c,amount):
        if(c.bal>=amount):
            c.bal -= amount
            print("Balance after withdraw is: ", c.bal)
        else:
            print("Insufficient amount in account. \nTransaction failed")

    def show(d):
        print(f"The account holder is {d.ac_holder} and the balance is {d.bal}")

#---------------------------------------

# e = Account('mira',5000)
# e.show()
# depoamount = float(input("Enter amount to deposit: "))
# e.deposit(depoamount)
# withamount = float(input("Enter amount to withdraw: "))
# e.withdraw(withamount)

#---------------------------------------

e = Account('mira',5000)

while True:
    print("----------------------------------------")
    inputs = int(input("Choose Option \n1. Deposit \n2. Withdraw \n3. Balance \n4. Exit \n")) 

    if(inputs == 1):
       depoamount = float(input("Enter amount to deposit: "))
       e.deposit(depoamount)
       
    elif(inputs ==2 ):
        withamount = float(input("Enter amount to withdraw: "))
        e.withdraw(withamount)
    
    elif(inputs == 3):
      e.show()

    elif(inputs == 4):
        print("Exit")
        break

    else:
       print("Incorrect Option")

