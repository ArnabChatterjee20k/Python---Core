def pat1(row):
    for i in range(1,row+1):
        for j in reversed(range(1,i+1)):
            print(j,end=" ")
        print()

def pat2(row):
    for i in range(1,row+1):
        for k in range(1,row+1-i):
            print(" ",end="")
        for j in range(1,i+2):
            print("*",end="")
        print()
    
r=int(input("rows="))
pat1(r)
pat2(r)
