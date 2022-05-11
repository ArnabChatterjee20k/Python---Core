class Num:
    count=0
    def __init__(self):
        Num.count+=1

n1=Num()
n2=Num()
n3=Num()

print("Instance created:",Num.count)
