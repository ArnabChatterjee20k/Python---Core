class computer:

    def __init__(self,cpu,ram):
        self.cpu=cpu #instance variable
        self.ram=ram


    def config(self):
        print("config is",self.cpu,self.ram)

com1=computer('i5',16)
com2=computer("i3",8)


com1.config()
com2.config()

print(com1.ram,com1.cpu)
print(com2.ram,com2.cpu)