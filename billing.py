m,n,l=[],[],[]
while 1:
	c=input("Item name?")
	print("Price of 1kg",c,"?")
	i=int(input())
	print("How much kg",c,"needed?")
	j=float(input())
	l.append(c)
	m.append(i*j)
	n.append(j)
	z=input("Want to add one more item in list (Y/N)?")
	if z=="n" or z=="N":
		break
	print("\n")
print()	
for i in range(len(l)):
	print(l[i],":",n[i],"kg   ",m[i],"rs")
print()           
print("Total cost:",sum(m))