def sort(n):
    l=[]
    for i in range(n):
        x=int(input("Enter the value of list"))
        l.append(x)
    print(l)
    for j in range(len(l)):
        for k in range(j):
            
            if l[j]>l[k]:
                l[j],l[k]=l[k],l[j]
    print(l)
    return l

n=int(input("Enter the length of list"))
sort(n)
