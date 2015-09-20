#n=5
n=int(input("Enter a number:"))
p=[]
for i in range(0 , n+1):
	p.append([])	
	p[i].append(1)
	if(i!=0):
		if(i!=1):
			for j in range(1,i):
				p[i].append(p[i-1][j-1]+p[i-1][j])
		p[i].append(1)
print(p)
m=n
for i in range(0,n):
	for j in range(0,m):
		print(" " , end=" ")
	#print("*")
	m-=1
	for no in p[i]:
		print(' ', no , end=" ")
	#print(p)
	print()
	
