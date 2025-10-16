#class is a blueprint for creating object
#method = function in class
#_init_ = initialize object attribute


#----------------------

# class Emp:
#     def display(self):
#         print("Display of employee class")
    
# e = Emp()
# e.display()

#----------------------

class Emp:
    def reg(self,eid,name):
        self.eid = eid
        self.name = name

    def display(self):
        print("Employee id ", self.eid)
        print("Employee name ", self.name)
    
e1 = Emp()
e2 = Emp()
e3 = Emp()
e1.reg(1,'mia')
e2.reg(2,'sara')
e3.reg(3,'nasuha')

print("Employee details as below:")
print("First Employee is:")
e1.display()
print("\nSecond Employee is:")
e2.display()
print("\nThird Employee is:")
e3.display()
