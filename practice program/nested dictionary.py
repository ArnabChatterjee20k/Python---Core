a={1:{2:[1 ,4,5],3:["a","f"],7:[1]}}
for i,j in a.items():
	pass
b=[]
for k in j.keys():
	b.append(k)
for l in b:
	print(j[l])
for l in b:
	for i in j[l]:
		print(i,end=" ")