#dicitonary = store key values, key is unique
#key value maping

# dictionary= [
#     {"id":'1', "name":'mira', "age":'18'},
#     {"id":'2', "name":'mara', "age":'28'},
#     {"id":'3', "name":'mia', "age":'38'},
#     {"id":'4', "name":'mirae', "age":'48'}
#       ]
      
# for k in dictionary:
#  print(k['id']+'->'+k['name'])

#----------add-----------------------

# employees= {"id":'1', "name":'mira', "salary":1800.50}
# # print("Employees details as below")

# for key, value in employees.items():
#     print(key, ":" , value)
  
# employees['city']="muscat"
# print("Dictionary after adding city")

# for key, value in employees.items():
#     print(key, ":" , value)


#-------delete--------------------------

# employees= {"id":'1', "name":'mira', "salary":1800.50}
# print("Employees details as below")

# for key, value in employees.items():
#     print(key, ":" , value)
  
# del employees["salary"]
# print("Dictionary after deleting salary")

# for key, value in employees.items():
#     print(key, ":" , value)

#----------print key only-----------------------

# employees= {"id":'1', "name":'mira', "salary":1800.50}

# for key in employees.keys():
#     print(key)

#---------print values only------------------------

employees= {"id":'1', "name":'mira', "salary":1800.50}

for key in employees.values():
    print(key)