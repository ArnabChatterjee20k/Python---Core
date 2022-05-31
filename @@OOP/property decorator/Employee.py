"""
    using property decorator we can use a method as an attribute.
    
    TODO: setter
    But we cant set value to it means if we do emp1.fullname = "arnab ch" then we
    will be getting error can't set attribute. 
    For this we need setter
"""
class Emp:
    def __init__(self,first,last ):
        self.first = first
        self.last = last
    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self,name):
        first , last = name.split(' ')
        self.first = first
        self.last = last

emp1 = Emp("arnab","ch")
print(emp1.email) # email is method but using property we can use it as an attribute
print(emp1.fullname)
emp1.fullname = "arnab ch"