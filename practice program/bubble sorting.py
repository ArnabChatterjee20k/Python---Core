l=[12,3,6,1,0]
for i in range(0,len(l)):
    for j in range(i):
        if l[i]<l[j]:
            #a=l[i]         can be
            #l[i]=l[j]      done in this way
            #l[j]=a
            l[i],l[j]=l[j],l[i]
print(l)
