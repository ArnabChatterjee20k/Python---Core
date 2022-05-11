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


class programmer(Employee):#inheriting super/parent class
    def __init__(self, fname, lname, salary,lang,exp):
        super().__init__(fname, lname, salary)
        self.lang=lang
        self.exp=exp
    
    # def increase(self):
    #     return super().increase()
    
    #method overriding
    def increase(self):#overiding the inherited instance method of superclass.
        self.salary=self.salary+300
    
help(programmer)#it returns none