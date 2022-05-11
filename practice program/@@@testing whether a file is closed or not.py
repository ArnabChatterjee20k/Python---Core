f=open("f.txt","w")
f.close()
for i in range(5):
    f=open("f.txt","w+")
    if i>1:
        
        break

    print(f.readable(),end=",")
    
print(f.closed)
f.close()
print(f.closed)
