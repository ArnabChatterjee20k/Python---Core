# using property decorator we can use a method as an attribute
class Emp:
    def __init__(self,first,last ):
        self.first = first
        self.last = last
    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"

emp1 = Emp("arnab","ch")
print(emp1.email) # email is method but using property we can use it as an attribute
