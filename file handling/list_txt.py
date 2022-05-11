import os
from tkinter import *
def ins(l,path):
    if os.path.exists(f"{path}"):
        with open(f"{path}") as f:
            for i in f.readlines():
                l.insert(END,i)
    else:
        print(f"{path} not found.")

def add(l,path):
    l.get(anchor)



