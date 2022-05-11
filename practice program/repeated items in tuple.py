from copy import deepcopy
t=(2,4,1,5,6,1,3,3,5,2,3,4,6)
b=list(t)
x=len(t)
a=deepcopy(b)
print(a)
for i in range(0,x):
    b.remove(b[i])
    if b[i] in a:
        c=b[i]
    print(c)
    
