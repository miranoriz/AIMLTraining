# tuple is ordered and mutable collection
#fixed data that should not be changed

# number = (1,2,3,4,5,4,3,4,6,7,7,5,4,3)
# print("The number in tuple is: ", len(number))
# for i in number:
#     print(i, end= " ")

#---------------find index of first occurence in tuple------------------------------

# number = (1,2,3,4,5,4,3,4,6,7,7,5,4,3)
# search_index = int(input("Enter number to find index: "))

# if search_index in number:
#     print(f"Index of {search_index} ", number.index(search_index))
# else:
#     print(f"No such {search_index} in tuple")

#---------------return number of occurence in tuple-------------------------------------------------

# number = (1,2,3,4,5,4,3,4,6,7,7,5,4,3)
# print("\nAll numbers in tuple: " , len(number))

# for num in number: 
#     print(num, end=" ")
# search_number = int(input("\nEnter number to find out frequency: "))

# if search_number in number:
#     print(f"Number {search_number} in tuple has the occurence of:  {number.count(search_number)} times")
# else:
#     print(f"Number {search_number} does not exist in tuple")


#-----------------write a program to sum a list with 4 numbers-----------------------------------------------

num = [1,3,4,5]
newnum = sum(num)
print(f"The result of sum in the list is {newnum}")


