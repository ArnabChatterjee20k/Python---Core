from functools import reduce

N = int(input())

list=[]

for i in range(N):
    z=int(input())
    list.append(z)
def add(x,y):
    return x+y
print(reduce(add,list))
