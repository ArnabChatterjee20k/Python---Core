class Employee:
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
    
    @staticmethod#independent function
    def welcome(name):
        print("welcome",name)

#simply run the static method by class name
Employee.welcome("Arnab")

#can work by making instance
Arnab=Employee("arnab","ch",30)
Arnab.welcome(Arnab.fname)


