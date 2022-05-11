import os
import datetime
import fontstyle

def dec():
    """to do Y/n"""
    dec.a = input("Want to do more(y/n)?")

def par():
    """to take input name and email"""

    par.name = input("Enter name:\t")
    par.email = input("Enter email:\t")




def subadd():
    par()
    """to write into files. """
    f = open("Student db.txt", "a")
    f.write(par.name + "\t" + par.email+"\n")
    f.close()
    dec()



def add():
    """to add into files"""
    loop=False
    # subadd()
    #
    # if loop==False and dec.a=="y"or"Y":
    #     subadd()
    #
    # else:
    #     pass
    if loop==False:
        subadd()
        dec()
        if dec.a=="y":
            subadd()
        else:
            loop=True

    choice()
def remove():
    e=input("Enter student name:")
    k=""
    f=open("Student db.txt","r+")

    for i in f:
        if i==e:
            k+=i


def choice():
    """to write into files according to decision"""

    if not os.path.exists("Student db.txt"):
        f=open("Student db.txt","x")
        f.close()
    choice.a=input(fontstyle.apply("1)Add\n2)Remove\n3)View\n4)Update\nEnter:\t","bold/underline/red"))
    if choice.a == "1":
        add()


choice()


