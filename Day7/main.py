#---------import file from other folder in the same directory-----

# from package import welcome # <--- from 'nama folder' import 'nama file'
# username = input("Enter your name: ")
# welcome.display(username)


# from package import student
# s1 = student.student(1,'mira') #<-- fileName.className()
# s1.print_info() #<-- function name


from package import calc 

num1 = int(input("Enter first num: "))
num2 = int(input("Enter second num: "))
result = calc.op()
print(' ', result.add(num1,num2))
