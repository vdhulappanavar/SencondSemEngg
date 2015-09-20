n=int(input("Enter the number of rows you want to print:"))
i=1
j=n
m=n
l=n
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
			#print("a + " , end='')
			print(chr(ord('a')+k) , " + " , sep='',end='')
		else:
			print(chr(ord('a')+k) , sep='',end='')
		k=k+1
	
	k=0
	while k<l:
		print(' ' ,end=' ')
		k=k+1
	print("=" , end=' ')
	l=l-1
	k=0
	while k<i:
		print(chr(ord('a')+k) , end='')
		k=k+1
	print()
	i=i+1
