# del:is used to delete the class

class Student:
    def __init__(self,name):
        self.name=name
s1=Student("prince")
print(s1.name)
del s1.name   #delete
del s1
print(s1.name)