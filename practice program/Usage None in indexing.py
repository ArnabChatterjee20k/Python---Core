# if a list is empty we cant use indexing but if it is populated with None then we can do the indexing means lst[12]
"""
    this will give error
    a =[]
    a[0] = error

    but if a = [None]
    a[0] = None
"""
right=[None]*10
for pi in range(1,10):
    right[pi-1]=("H"+str(pi))
    pi+=1
print(right)
