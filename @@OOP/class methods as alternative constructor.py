class Employee:
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
    
    @classmethod
    def from_str(cls,emp_str):
        """cls is class"""
        fname,lname,salary=emp_str.split("-")
        return cls(fname,lname,salary)#cls is class. We r doing the normal construction indirectly by classmethod.string will be parsed and  will be evaluated in Employee class as Employee(fname,lname,salary)


Arnab=Employee("arnab","ch",30)#by init constructor
bittu=Employee.from_str("bittu-ch-399")#by classmethod
