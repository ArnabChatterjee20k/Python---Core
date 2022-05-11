from tkinter import *

w= Tk()
a={1:{"c":[1,2,3,5],"d":[4,7,3],"e":[0,10,30]}}
l=Listbox(w)

for b in a:
    c=a[b]
    print(c)
q=[]
for key in c.keys():
    print(key)
    q.append(key)
print(q)

for i,j in a.items():
    pass

for k in range(len(q)):
    l.insert(END,q[k])
    for m in j[q[k]]:
        l.insert(END,m)
l.pack()
w.mainloop()

