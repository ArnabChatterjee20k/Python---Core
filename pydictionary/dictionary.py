import PyDictionary  as p
from tkinter import *
from tkinter import ttk
w=Tk()
w.title("Pocket dictionary coded by Arnab Chatterjee")
w.geometry("500x600")
w.resizable(0,0)
x=StringVar()
y=StringVar()
# expression=""

def click():
    """It will  get clicked and show the meaning in the label"""
    """Used listbox instead of label or entry to print meanings as set method will replace words one by one and the last meaning will only printed. Thus listbox is used for its insert function """

    # global expression

    # button=x.get()
    # print(x.get())

    lb.delete(0, END)######## to clear the screen

    dic = p.PyDictionary(x.get())
    meaning = dic.getMeanings()

    print(meaning)
    try:
        b=meaning[x.get()]["Noun"]
        print(b)

        l=len(b) #### to get the range of a list
        for i in range(0, l):###itering through the list of noun
            print("Noun\n",b[i] + "\n")
            # y.set(b[i])###only the last  text will be appeared as it set is a replacing process
            lb.insert(END,(b[i]))
        lb.insert(0,"Noun::")
    except:
        print("Noun not present")
        lb.delete(0)

    lb.insert(END, "\n")###to make a gap bw noun and verb
    lb.insert(END,"Verb::")########## to print the verb section after the  noun section

    try:

        b=meaning[x.get()]["Verb"]
        l = len(b)
        for i in range(0, l):
            print("Verb\n",b[i] + "\n")
            lb.insert(END, (b[i]))

    except:
        print("Verb not present")
        lb.delete(END)
    # lb.delete(0, END) will not get inserted  in the list so better  to clean the list everythong  before insertion




Label(w, text='Word',font="TimesNewRoman 24 bold").place(x=0,y=0)

e1 = Entry(w,justify="center",borderwidth="10",font=("","20","bold"),textvariable=x).place(x=100,y=0)


b1=Button(w,text="Search",font=("","20"),command=click)#####dont use click() as it will not work

b1.place(x=80,y=70,width="100",height="70")

# a=Entry(w,justify="center",borderwidth="10",font=("","10","bold"),textvariable=y)
# a.place(x=0,y=170,width="500",height="170")

#### scroll bar
SVBar = Scrollbar(w)
SVBar.pack(side=RIGHT,fill="y")
SHBar = Scrollbar(w,orient=HORIZONTAL)

SHBar.pack(side=BOTTOM,fill="x")


lb=Listbox(w,width=68,height=20,font=("Arial 10 bold"),yscrollcommand = SVBar.set,xscrollcommand = SHBar.set)

####### func of scroll bars
SVBar.config(command = lb.yview)
SHBar.config(command = lb.xview)


lb.place(x=0,y=180)
opt=["Eng to Eng","Eng to "]
format=ttk.Combobox(w,textvariable=y)
format.place(x=200,y=90)
w.mainloop()

