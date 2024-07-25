#inhertitance=inhert the property of parent class or child class inhert the property of base class

class car:
    def start(self):
        print("start the car")
    def restart(self):
        print("restart...")
class toyta(car):
    def __init__(self,name):
        self.name=name
      
car1=toyta("swift")
print(car1.restart())
print(car1.name)

    
