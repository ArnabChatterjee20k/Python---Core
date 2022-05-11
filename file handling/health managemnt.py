import os
def name():
    if not os.path.exists("name.txt"):
        name.a=input("Enter customer name:")
        name.b=input("Enter customer name:")
        name.c=input("Enter customer name:")
        name_file=open("name.txt","x")
        name_file.close()
        name_file=open("name.txt","a")
        name_file.write(name.a+"\n")
        name_file.write(name.b+'\n')
        name_file.write(name.c+"\n")
        name_file.close()

    p=name.a
    q=name.b
    r=name.c



def file():
    ### the commented code will only work once that is when they are created first then due to f name.a is not present
    # file.f=open(name.a+".txt","x")
    # file.g=open(name.b+".txt","x")
    # file.h=open(name.c+".txt","x")
    #
    # file.f.close()
    # file.g.close()
    # file.h.close()

    file.f= open("name.txt","r+")
    a = file.f.readline()
    b = file.f.readline()
    c = file.f.readline()
    file.f=open(p+".txt","x")
    file.g=open(str(b)+".txt","x")
    file.h=open(str(c)+".txt","x")



    file.f.close()
    file.g.close()
    file.h.close()
def subchoice(n):
    import datetime
    x = datetime.datetime.now()
    sub = input("Enter food/exercise:\t")
    if sub == "food":
        entry1 = input("Enter the food:\t")
        f=open(n+"food.txt","a")
        f.write("[" + x + "]"+ entry1)
        f.close()
        file.f = open(name.n+".txt", "a")
        file.f.write("["+ x + "]"+"entry done for food")
        file.f.close()
    elif sub == "exercise":
        entry2 = input("Enter the exercise:\t")
        f = open(n + "exercise.txt", "a")
        f.write(str(str(x))+ entry2)
        f.close()
        file.f = open(name.n + ".txt", "a")
        file.f.write("["+ str(x) + "]"+ "entry done for food")
        file.f.close()

def choice(ch):

    if ch == a:
        subchoice(a)
    if ch == b:
        subchoice(b)
    if ch == c:
        subchoice(c)

# try:
#     file()
#     name()
#
#

#
#     print("Name\n",name.a,"\n",name.b,"\n",name.c)
#
#     ch=input("Enter log:\t")
#
#     choice(ch)
#
# except Exception as ex:
#     print(ex)   ### printing the error if occured


name()

name_file = open("name.txt", "r")
print("Name\n\n", name_file.read(), "\n",name_file.read(), "\n", name_file.read())
name_file.close()

file()

# a=name.a
# b=name.b
# c=name.c


ch=input("Enter log:\t")

choice(ch)
