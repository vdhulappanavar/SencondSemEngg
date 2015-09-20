n=int(input("Enter the number of rows you want to print:"))
i=0
j=n
m=n
while i<=n:
	while j>=0:
		print(' ' , end=' ')
		j=j-1
	m=m-1
	j=m
	#print("1")
	k=0
	while k<i:
		#print( "not" , k ,"==(" , i-1 , ")=" ,not k==(i-1))
		if(not k==(i-1)):
			print("a + " , end='')
		else:
			print("a " , end='')
		k=k+1
	print()
	i=i+1
