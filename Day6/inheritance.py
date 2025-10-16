#inheritance = no need to rewrite the same function in other class 

#superclass --> 
class Emp(): 

    def reg(self,id,name):
        self.id = id
        self.name = name

    def display(self):
        print (f"ID: ",self.id)
        print (f"Name: ",self.name)

#child class --> 
class dev(Emp):

    def welcome(self):
       print("Welcome to inheritance")
    

d = dev()
d.welcome()
d.reg(1,"Sam")
d.display()

e = dev()
e.reg(2,"mira")
e.display()