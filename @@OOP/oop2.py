class car:
    wheels=4#class variable
    def __init__(self):
        self.com="BMW"#instnace variable
        self.mil=8#instnace variable


c1=car()
c2=car()
c1.com="audi"
car.wheels=6

print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil,c2.wheels)