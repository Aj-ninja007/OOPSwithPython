#abstraction -> hiding the unecessary part or implementaion part in a class and show the essential part to the user


class car:
    def __init__(self):# constructer->default  constructer
        self.acc=False
        self.catch=False
        self.br=False
    def start(self):
        self.catch=True
        self.br=True
        self.acc=True
        print("car is started..")
c1=car()
c1.start()       #car is started..



# encapsulation ->wrapping data and  functions into single unit(object)  