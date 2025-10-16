#polymorphism = allow method to have different implementation based on object
#call another function in super class. 

# class Bird():
#     def fly(self):
#         print("Bird can fly")


# class Airplane(Bird):
#     def fly(self):
#       print("Airplane fly")

# b=Bird()
# print('bird implementation')
# b.fly()

# print('airplane implementation')
# a=Airplane()
# a.fly()

# print("-----------")
# for obj in[Bird(), Airplane()]:
#     obj.fly()


#---------------------------------------------

class Emp():
  
  def reg(self):
    self.id = int(input("Enter ID: "))
    self.name = input("Enter Name: ")


  def display(s):
     print("ID: ", s.id)
     print("Name: ", s.name)

class Dev(Emp):
    def reg(self):
       super().reg()
       self.domain = input("Enter domain: ")

    def disp(s):
       super().display()
       print("Domain : ", s.domain)

d = Dev()
d.reg()
d.disp()

