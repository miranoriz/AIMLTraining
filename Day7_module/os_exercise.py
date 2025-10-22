#-----------rename a folder in current directory---------------

# import os 

# cdir = os.getcwd() #<--get current working directory
# folder_name = input("Enter folder name to be rename: ")
# newname = input(f"Enter new name for {folder_name}: ")
# folder_path = os.path.join(cdir,folder_name)

# if(os.path.exists(folder_path)):
#     os.rename(folder_name, newname)
#     print(f"{folder_name} has been renamed to {newname}")
# else:
#     print("Folder does not exist")

#----import function from another main file in same directory-------------

import calc
import module

firstnum = int(input("enter first number: "))
secondnum = int(input("enter second number: "))
print(f"Total number of {firstnum} and {secondnum} is ", calc.add(firstnum,secondnum)) #<-- function from first file
module.winner() #<-- function from second file

#----import function from another file in other directory-------------




