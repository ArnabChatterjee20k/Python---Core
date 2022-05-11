import tkinter as tk
from tkinter import StringVar, Tk, ttk
from tkinter.constants import CENTER
import PIL
import requests,imutils
from PIL import ImageTk,Image

class Window(tk.Tk):
    img=Image.open("images/hills.png")
    img=img.resize((490,800), Image.ANTIALIAS)
    def __init__(self):
        super().__init__()
        self.bg=ImageTk.PhotoImage(Window.img)
        self.geometry("500x500")
        self.title("Image Downloader")
        self.bgimg=ttk.Label(self,image=self.bg,compound=CENTER)
        self.bgimg.place(x=0,y=0)
        # self.attributes("-alpha",0.9)
        
        self.options=[]
        self.var=StringVar()
        self.drop=ttk.Combobox(self,textvariable=self.var,values=self.options)
        self.drop.place(x=150,y=30)
        self.optionlabel=ttk.Label(self,text="Enter the image").place(x=30,y=30)

        
root=Window()
root.mainloop()