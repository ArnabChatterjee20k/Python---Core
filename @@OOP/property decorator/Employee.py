"""
    using property decorator we can use a method as an attribute.
    
    TODO: setter
    But we cant set value to it means if we do emp1.fullname = "arnab ch" then we
    will be getting error can't set attribute. 
    For this we need setter

    TODO: deleter
    If we want to do a clean up code when we are deleting the attributes we can use it
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

    @fullname.deleter
    def fullname(self):
        print("Delete name")
        self.first = None
        self.last = None

emp1 = Emp("arnab","ch")
# using property
print(emp1.email) # email is method but using property we can use it as an attribute

# using setter
print(emp1.fullname)
emp1.fullname = "arnab ch"

#using deleter
del emp1.fullname
print(emp1.fullname)