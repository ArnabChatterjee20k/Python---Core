f=open("file.txt","rt")## f is the file pointer
cnt1=f.read()
print(cnt1)
f.close()

f=open("file.txt","rb")##binary mode
cnt2=f.read(2)
print(cnt2)
f.close()

f=open("file.txt","rt")###default one
cnt3=f.read(6)
print(cnt3)
cnt3=f.read(11)
print(cnt3)
f.close()

f=open("file.txt")###default one
cnt4=f.readline()#read individual lines
print("new",cnt4)
print("new1",f.readline())
###one gap is due to the new line in output and it is shown in readlines

print("new2",f.readline())

print("new3",f.readline())
#in readlines it will start from nxt after the readline.
print("new4",f.readlines())
print(f.readlines())#blank list
f.close()

f=open("file.txt","rb")
print("neeeew",f.readlines(50))
# The readlines() method returns a list containing each line in the file as a list item. Use the hint parameter to limit the number of lines returned. If the total number of bytes returned exceeds the specified number, no more lines are returned.
f.close()

f=open("file.txt","rt")
for i in f:
    print(i,end="")
f.close()

f=open("file.txt","rt")
x=f.read()
for i in f:####not will get printed as f is empty
    print("n",x)
f.close()
###some other things available in d drive