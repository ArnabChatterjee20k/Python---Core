from tkinter import *

top = Tk()
Lb = Listbox(top)
a={1:{"c":[1,2,3,5],"d":[4,7,3],"e":[0,10,30]}}#### i=1 and  j is the nested dictionary

m=[]########### for storing the sub keys
### to store sub keys
for q in a:
    for o in a[q]:
        m.append(o)
print(m)

for i,j in a.items():
    print(j)
    pass

# for l in range(len(m)):                          ###### l=0, m[l]=c ,j[m[l]]= j[c]= [1 2 3 4 5]
#     Lb.insert(END,m[l])
#     Lb.insert(END,j[m[l]])

for l in range(len(m)):                          ###### l=0, m[l]=c ,j[m[l]]= j[c]= [1 2 3 4 5],k=1,2,...
    Lb.insert(END,m[l])
    for k in j[m[l]]:
        Lb.insert(END,k)


Lb.pack()
top.mainloop()