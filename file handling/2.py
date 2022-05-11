import csv
# with open("2.csv",newline="") as f:
#     file=csv.DictReader(f)
#     for i in file:
#         print(i)
# with open("2nd.csv",newline="") as f:
#     file=csv.DictReader(f)
#     for i in file:
#         print(i)
#         print("Value stored in 1:",i["1"])

with open("2.csv",newline="") as f:###headers or 1st row msut be uinque.
        for i in csv.DictReader(f):
            print(i)