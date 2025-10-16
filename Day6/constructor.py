class Emp():
   def __init__(self,id,name,qual='MIC'): #<----- auto assign if blank
      self.id = id
      self.name = name
      self.qual = qual

   def disp(s):
     print("ID: ", s.id)
     print("Name: ", s.name)
     print("Qualification: ", s.qual)
   
class Dev(Emp):
   
   def __init__(self,id,name,qual,domain,project):
      super().__init__(id,name,qual) #<--- tak perlu letak self. letak attribute sahaja
      self.domain = domain
      self.project = project

   def display(self):
      super().disp()
      print("Domain: ", self.domain)
      print("Project: ", self.project)

#create one Emp object with id=1, name=sam, qual=MCA
#create one Dev object with id=3, name=ravi, qual=Mtech. domain=Eshopping, Project=dot net

e=Emp(1,'sam')
e.disp()

d=Dev(3,'ravi','Mtech','eshopping','dot net')
d.display()
