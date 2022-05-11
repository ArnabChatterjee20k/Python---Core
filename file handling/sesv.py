import csv
# with open('1st.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#          print(', '.join(row))
import csv
a=["ad"]
with open('eggs.csv', 'r+',newline="") as csvfile:#if newline not specified empty lists will be generated.
    r=csv.reader(csvfile)
    w=csv.writer(csvfile,dialect="excel")#default excel
    w1=csv.writer(csvfile,dialect="excel-tab")
    w2=csv.writer(csvfile,dialect="unix")
    w.writerow(a)
    w1.writerow("ar")
    w2.writerow("ar6")
    w.writerow(["ar"])
    for i in r:
        print(i)

# csv.list_dialects() to see dialects.


