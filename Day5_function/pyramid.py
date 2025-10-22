
# ------------------------------------

#big base and all star

# def pyramid(num):
#     for i in range(1, num+1):
#       print(" " * (num-i), end=" ")
#       print("*" * (2*i-1))
    
# pyramid(6)


# ------------------------------------

#big base and all number

# def pyramid(num):

#     for i in range(1, num+1):
#         print(" "*(num-i),end=" ")
#         print(str(i)*(2*i-1))

# number = int(input("Enter a number: "))
# pyramid(number)

# ------------------------------------

#narrow base and all star

def pyramid(num):
    for i in range(num, 0,-1): #start from num to down
      print(" " * (num-i), end=" ")
      print("*" * ((2*i-1)))
    
# number = int(input("Enter a number: "))
# pyramid(number)

# ------------------------------------

#narrow base and all number

def pyramid(num):
    for i in range(num, 0,-1):
      print(" " * (num-i), end=" ")
      print(str(i) * ((2*i-1)))
    
number = int(input("Enter a number: "))
pyramid(number)