import csv
old_data=[]
n=1
##STORING DATA
with open("2.csv","r",newline="") as f:
    read=csv.reader(f)
    for i in read:
        print(n,")",i)
        old_data.append(i)
        n+=1
##MANIPULATING STORED DATA
x=int(input("Enter the sl no. : "))
b=old_data[x-1]
print(b)
length=1
new_data=[]
while length<len(b):
    # if length==len(b):
        # break
    for i in b:
        data=input(f"{i}= ")
        if data=="" or data==" ":
            data=i
        new_data.append(data.strip())
        length += 1
    old_data[x-1]=new_data
    print(old_data)
## WRITING STORED DATA TO THE CSV FILE
with open("2.csv","w",newline="") as f:
    for i in old_data:
        csv.writer(f).writerow(i)##here delimiter=" " will remove komas. default is delimiter=","


# with open("2.csv","w",newline="") as f:
#     writer=csv.writer(f)


# print(a)

# for i in range(3):
#     pass
# print(a[i])

# for i in a:
#     print(i)
#     if a.index(i)==0:
#         break

