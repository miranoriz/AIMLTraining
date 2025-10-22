
#-----------------------create folder inside current directory--------

# import os
# cdir = os.getcwd()
# folder_name = input("Enter folder name to create: ")
# folder_path = os.path.join(cdir,folder_name )

# if (os.path.exists(folder_path)):
#     print("Folder already exist")
# else: 
#     os.makedirs(folder_path,exist_ok=True) #<---- create folder
#     print(f"{folder_name} created at {folder_path}" )

#--------------------------rename a folder------------------------------

# os.rename(folder_name, "renamed_folder")

#-------------------------create file inside current directory and rewrite---------

#The with statement ensures the file is automatically closed after the block runs — even if there’s an error.
#w - write mode
#a - append mode
#x - create new file
#r - read mode

newfile = input("Create new file: ")

try:
    with open(newfile, "x") as file:
     file.write("This file is guaranteed to be new.")
     print(f"File {newfile} created successfully.")
except FileExistsError:
    print(f"File {newfile }already exists.")