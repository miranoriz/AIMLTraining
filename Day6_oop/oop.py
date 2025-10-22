#class is a blueprint/template for creating object
#method = function in class
#_init_ = initialize object attribute


#----------------------

# class Emp:
#     def display(self):
#         print("Display of employee class")
    
# e = Emp()
# e.display()

#----------------------

# class Emp:
#     def reg(self,eid,name):
#         self.eid = eid
#         self.name = name

#     def display(self):
#         print("Employee id ", self.eid)
#         print("Employee name ", self.name)
    
# e1 = Emp()
# e2 = Emp()
# e3 = Emp()

# e1.reg(1,'mia')
# e2.reg(2,'sara')
# e3.reg(3,'nasuha')

# print("Employee details as below:")
# print("First Employee is:")
# e1.display()
# print("\nSecond Employee is:")
# e2.display()
# print("\nThird Employee is:")
# e3.display()


#----------------------

#initalize the object
#object creation

# class Player(): 

#     def __init__(s):
#         print("welcome to constructor")

#     def reg(self,id,name,team):
#         self.id = id
#         self.name = name
#         self.team = team

#     def display(self):
#         print(f"ID: {self.id} , Name: {self.name} , Team: {self.team}")
    
# p1 = Player()
# p2 = Player()
# p3 = Player()

# p1.reg(1,'mira','mas')
# p2.reg(2,'maya','ind')
# p3.reg(3,'mmohd','sg')

# p1.display()
# p2.display()
# p3.display()

#-------------------------------------------------------

#__str__ is define how an object should appear when converted to a string for end-users

# class Player(): 

#     def __init__(self,id,name,team):
#         self.id = id
#         self.name = name
#         self.team = team

#     def __str__(self):
#         return f"ID: {self.id} , Name: {self.name} , Team: {self.team}"
    
# p1 = Player(1,'mira','mas')
# p2 = Player(2,'maya','ind')
# p3 = Player(3,'mmohd','sg')

# print(p1)
# print(p2)
# print(p3)



