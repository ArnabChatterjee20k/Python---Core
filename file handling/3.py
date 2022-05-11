import csv,win32
# with open("2.csv")as f:
#     for i in csv.DictReader(f):
#         for j in i:
#             print(i)
#             print(j,":",i[j])
#             print("_______")
# # a=["aaa"]
# # with open("3.csv","w",newline="") as f:
# #     e=csv.DictWriter(f,["at","ww"])
# #     e.writeheader()
# #     e.writerow({"at":"a","ww":"s"})
# #     e.writerow({"at": "a"})
#
# fieldname=["A","B","c","D"]
# data=["a","b","e","r"]
# r={"A":"a","B":"b"}
# with open("dict.cv", "w", newline="") as f:
#     writer = csv.DictWriter(f, fieldnames=fieldname)
#     writer.writeheader()
#     writer.writerow(dict(zip(fieldname,data)))
with open("2.csv")as f:
    field=csv.DictReader(f)
    for i in field.fieldnames:
        print(i,end="  ")
    print()
    print("_______", end="  ")
    for j in field:
        print()
        # print(j)
        for k in j:
            print(j[k],end="  ")