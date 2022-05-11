# required ds===  a=[ 
#                     [ [],[] ] , 
#                     [ [],[] ]  
#                   ]

#  [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]]


a=[] #making outer structer

# at every iteration a list will be appended then 2 list will be extended inside the appended list then another will loop will run to isnert data inside the 2 extended list

for i in range(1,10):
    a.append([])#making inner structer
    a[len(a)-1].extend([[],[]]) #extending list at the last list element of a.
    for j in range(1,10):
        a[len(a)-1][0].append(j)
        a[len(a)-1][1].append(j)
a[0][0]=[12.12221]
print(a)
print(a[3])


for i,j in enumerate(a):
    print(i,j)
    
print("\n\n\n")
    
for i,j in enumerate(a):
    if j==[1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print("y")
        print(i,j[:][0])
    else:
        print("no")

print("\n\n\n")

for i,j in enumerate(a):
    j[0].pop(0)
    print(j[0])



for i,j in enumerate(a):
    if j[0]==[12.12221]:
        print("y")
    elif j[0]==[1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print("as")
    #for k in j:
    #   print(k)


# j[:] means [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]]

# j[:][0] means [1, 2, 3, 4, 5, 6, 7, 8, 9]
