from  list_txt import ins
from  tkinter import  *
w=Tk()
w.title("ARNAB")
l=Listbox(w)
l.pack()
ins(l=l,path="D:\Python\PROJECT MANAGER\ongoing\Time.txt")
w.mainloop()