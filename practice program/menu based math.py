
def choice(n):
    if n==1:
        rec()
    elif n==2:
        cir()
    else:
        print("Error")
             
    
def rec():
    l=int(input("Enter the length="))
    b=int(input("Enter the breadth="))
    a=l*b
    print("Area:",a)
    

def cir():
    r=int(input("Enter the radius="))
    a=3.14*(r**2)
    print("Area:",a)
    
menu={1:"Area of rectangle",2:"Area of circle"}

print("Menu\n\nOption\t\t\tChoice")
for i in menu:
    print(i,'\t\t',menu[i])

n=int(input("\n\nEnter the option"))
choice(n)



