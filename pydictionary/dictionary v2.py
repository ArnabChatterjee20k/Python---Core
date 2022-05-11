import PyDictionary  as p
from tkinter import *
from tkinter import ttk

w = Tk()
w.title("Pocket dictionary coded by Arnab Chatterjee")
w.geometry("500x600")
w.resizable(0, 0)
x = StringVar()
y = StringVar()

def click():
    """It will  get clicked and show the meaning in the label"""
    """Used listbox instead of label or entry to print meanings as set method will replace words one by one and the last meaning will only printed. Thus listbox is used for its insert function """


    lb.delete(0, END)  ######## to clear the screen

    dic = p.PyDictionary(x.get())
    meaning = dic.getMeanings()

    if y.get() == "Eng to Eng":
        keys = []

        for a in meaning[x.get()]:
            keys.append(a)


        for i, j in meaning.items():
            pass

        for l in range(len(keys)):
            lb.insert(END, keys[l])
            lb.insert(END,"\n")#### to give space bw headings and words
            for k in j[keys[l]]:
                lb.insert(END, k)
            lb.insert(END, "\n")### to give space between words and headings

    elif y.get()=="Eng to Bengali":
        lb.insert(END,dic.translateTo("bn"))

    elif y.get()=="Eng to Hindi":
        lb.insert(END,dic.translateTo("hi"))



    # lb.delete(0, END) will not get inserted  in the list so better  to clean the list everythong  before insertion
Label(w, text='Word', font="TimesNewRoman 24 bold").place(x=0, y=0)

e1 = Entry(w, justify="center", borderwidth="10", font=("", "20", "bold"), textvariable=x).place(x=100, y=0)

b1 = Button(w, text="Search", font=("", "20"), command=click)  #####dont use click() as it will not work

b1.place(x=80, y=70, width="100", height="70")



#### scroll bar
SVBar = Scrollbar(w)
SVBar.pack(side=RIGHT, fill="y")
SHBar = Scrollbar(w, orient=HORIZONTAL)

SHBar.pack(side=BOTTOM, fill="x")

lb = Listbox(w, width=68, height=20, font=("Arial 10 bold"), yscrollcommand=SVBar.set, xscrollcommand=SHBar.set)

####### func of scroll bars
SVBar.config(command=lb.yview)
SHBar.config(command=lb.xview)

lb.place(x=0, y=180)
opt = ["Eng to Eng", "Eng to Bengali", "Eng to Hindi"]
format = ttk.Combobox(w, textvariable=y,values=opt)
y.set("Eng to Eng")
format.place(x=200, y=90)

Label(w,text="Translations",font="Arial 10 bold").place(x=230 , y=60)

w.mainloop()

