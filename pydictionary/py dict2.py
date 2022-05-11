import  PyDictionary
# d= PyDictionary.PyDictionary()
# a=input("Enter: ")
# print(d.meaning(a))


d= PyDictionary.PyDictionary("endeavour")
# print(d.printMeanings())
# print(d.getMeanings())

# another way to print dictoionars meanings
a=d.getMeanings()
print(type(a))
for i in a:
    print(a[i])
    print(a[i]["Noun"])

###################################################################
x=a[i]["Noun"]
q=len(x)
for i in range(0,q):
    print(x[i]+"\n")


