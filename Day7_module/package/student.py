class student:

    def __init__(self, id, name):
        #pass # <-- if we want to leave it blank
        self.id = id
        self.name = name

    def print_info(self):
        print("Student ID: " , self.id)
        print("Student Name: ", self.name)

