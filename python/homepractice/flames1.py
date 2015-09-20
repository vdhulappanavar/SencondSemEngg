"""n1=input("Enetr 1st name:")
n2=input("Enter 2nd name:")
efflen=len(n2)+len(n1)
print(efflen)
n3,n4=n1,n2
for i in n3:
	for j in n4:
		#print("i=" , i , "j=" , j)
		if i==j:# and n4.count(j)==1:
			efflen-=2
			break
		else:
			print(i,j,end=' ')
	print()
			
print("Efflen=" , efflen)
	"""	
""""c=list(n1+n2)
d=set(c)
print(c)
print(d)
efflen=len(n2)+len(n1)
for i in d:
	efflen-=2*(c.count(i)//2)
print(efflen)"""


n1=input("Enetr 1st name:")
n2=input("Enter 2nd name:")
efflen=len(n1)+len(n2)
a=[list(n1) , list(n2)]
b=set(n1+n2)
for i in b:
	#print(a[0].count(i))
	#print(a[1].count(i))
	c=a[0].count(i)
	d=a[1].count(i)
	efflen-=2 
print(efflen)