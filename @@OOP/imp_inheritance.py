class A():
    name="ClassVar"
    def __init__(self):
        self.name="Instance/Obj Var"

class B(A):
    name="Derived class"

objA=A()
print(objA.name)#Instance/Obj Var

objB=B()
print(objB.name)#Instance/Obj Var
