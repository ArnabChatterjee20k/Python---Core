# try:
#
#     a={1:{2:3,5:4,"verb":6}}
#     b=a.values()#####returns a list
#     for i in b:
#         print(i)######## return the sub dictionary
#     for j in i:
#         print("Keys:::\n",j)#### return the keys of sub dictionary
#         print("Values:::\n",j,i[j])##### as i contains  the sub dictionary
#         k=[j]
#         print(k)
#
#
#         if "verb" in k:
#             print("yes","verb",i["verb"])
# except:
#     print("ok")

a={1:{"c":[1,2,3,5],"d":[4,7,3],"e":[0,10,30]}}

for i in a:
    print(i)
    print(a[i])

b=a[i].keys()
print(b)
q=[]

for c in b:
    q.append(c)
print(q)


# for j in a[i]:
#
#     print(j,":",a[i][j])
#
# #### same
# for i,j in a.items():
#     print(i)
#     print(j)
# for k in j :
#     print(k,":",j[k])



