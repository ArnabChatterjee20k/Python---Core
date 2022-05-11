a=input("Enter file name:")
f=open(a+".txt","a")
b=input("""Enter text: """)
f.write(b)
f.close()

