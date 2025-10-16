#print("welcome to day 3: data structure")

#list = an order of mutable collection, have index starting from 0
#general purpose ordered data

# my_list = [10,20,30,"python",None,True,12,45]
# print("number of item in list are: ", len(my_list))
# for item in my_list:
#     print(item)

# employees = ['maya', 'aya', 'zira', 'kina', 'pors', 'kisha', 'iqa']
# print("\nNumber of employees is : ", len(employees))
# print("Details of employees is as below: ")
# for i in employees:
#    print(i, end = " ")
# print("\n")

#-----------------------sort = arrange list in particular order------------------------------

# employees = ['maya', 'aya', 'zira', 'kina', 'pors', 'kisha', 'iqa']
# print("\nList BEFORE sorting")
# for i in employees:
#     print(i, end=" ")
# print("\n")
# employees.sort()
# print("List AFTER sorting")
# for e in employees:
#     print(e, end=" ")
# print("\n")

# employees = ['maya', 'aya', 'pors', 'kisha', 'iqa']
# print("\nList BEFORE sorting")
# for i in employees:
#     print(i, end=" ")
# print("\n")

# print("List AFTER sorting")
# employees.reverse()
# for e in employees:
#     print(e, end=" ")


#--------------------append------------------------------------------------------------

# employees = ['maya', 'aya', 'pors', 'kisha', 'iqa']
# newemp = input("Enter New Employee")
# employees.append(newemp)
# for emp in employees:
#     print(emp, end=" ")

#--------------------insert------------------------------------------------------------

# employees = ['maya', 'aya', 'pors', 'kisha', 'iqa']
# newemp = input("Enter New Employee")
# pos = int(input("Enter position"))
# employees.insert(pos, newemp)

# for emp in employees:
#     print(emp, end=" ")

#-------------------remove-------------------------------------------------------------

# employees = ['maya', 'aya', 'pors', 'kisha', 'iqa']
# delInput = input("Employee to remove from the list : ")


# if delInput in employees: 
#   employees.remove(delInput)
#   print("Number of employees after deleting {delInput} in list are: ", len(employees))
#   for emp in employees:
#     print(emp, end=" ")
# else:
#   print("The employees is not exist")

#--------------------pop------------------------------------------------------------

# employees = ['maya', 'aya', 'pors', 'kisha', 'iqa']
# del_index = int(input("Enter index to pop item : "))
# print("Pop result : ", employees.pop(del_index))
# print("Number of employees after pop() are: ", len(employees))
# for emp in employees:
#     print(emp, end=" ")

#--------------------find first and last element from the list---------------------

# employees = ['maya', 'aya', 'pors', 'kisha', 'iqa']
# print("number of employess: " , len(employees))

# for emp in employees:
#    print(emp, end=" ")

# print("\nFirst element in employees is: ", employees[0])
# print("Last element in employees is: ", employees[-1])
