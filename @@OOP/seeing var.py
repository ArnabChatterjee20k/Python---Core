class add:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def s(self):
        return self.a+self.b

q=add(1,2)
w=add(2,3)
print(q.s()+w.s())

print(q.__dict__)#variables of instance q
print(add.__dict__)#variables of class add