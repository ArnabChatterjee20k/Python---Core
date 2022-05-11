class Add:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def __repr__(self) :
        return f'{self.a+self.b}'

num = Add(1,2)
if __name__ == "__main__":
    print("module.py",num)
