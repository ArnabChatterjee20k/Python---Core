from PyDictionary import *

d=PyDictionary("endeavour")
a=d.getMeanings()
for i in a:
    # print(i)
    # print(a[i])
    # pass
    b = a[i]
    # print(b)
print(b)
###transversed in key "endeavour" and  then storing the  inner dic in b
# b=a[i]
# for k in b:
#     print(k)
#     print(b[k])

# In list format
# print("\nNoun","=", b["Noun"])
# print("\nVerb","=", b["Verb"])

for j in b["Noun"]:
    Noun=j

print("\nNoun","=", Noun)######without list in string format

print(a["endeavour"]["Noun"])