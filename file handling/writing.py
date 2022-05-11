#f=open("writing.txt","w")
#f.write("Each time it will get replaced by this text in writing mode")
#a=f.write("Each time it will get replaced by this text in writing mode")
#print("No. of characters:-",a)
#f.close()

# f=open("writing.txt","a")##append
# a=f.write("Now each time it will this text\n")
# print("No. of characters wrote:-",a)
# f.close()

# f=open("writing.txt","r+")## read + write
# print(f.read())
# f.write("its append + read")
# f.close()

# import os
# if not os.path.exists("writing.txt"):
#     f=open("writing.txt","x")
#     f.close()
# f=open("writing.txt","a")
# f.write("aaaa")
# f.close()

#### writing takes one arguemnt so to give \n use + instead of ,



# reading the file r+ will append along with read
# f=open("writing.txt","r+")
# f.write("ssss\n")
# a=f.readline()
# b=f.readline()
# c=f.readline()
# print(a,b,c)
#
# f.close()


