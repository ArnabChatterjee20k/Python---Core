## 0 1 1 2 3 5 8 13

l=[0,1]

for i in range(2,6):
    l.append((i-1)+(i-2))
print(l)### returning a list
q=filter(lambda e:e in l,l)
print(tuple(q))###returning a tuple
