class Employee:
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
    
    @classmethod
    def from_str(cls,emp_str):
        """cls is class"""
        fname,lname,salary=emp_str.split("-")
        return cls(fname,lname,salary)
    
    def increase(self):
        self.salary=self.salary+100

    def __add__(self,other):
        """Overwriting add method"""
        return self.salary+other.salary

    def __repr__(self):
        """Overwriting print function"""
        return f"Employee name is {self.fname + self.lname}"
    
    def __str__(self):
        return self.fname
Arnab=Employee("Arnab","Ch",20000)
Bittu=Employee("Bittu","Ch",39999)

print(Arnab+Bittu)
print(repr(Arnab))
print(Arnab)#since str method it will work differently if not defined then it would work same as print(repr(Arnab))
print(str(Arnab))