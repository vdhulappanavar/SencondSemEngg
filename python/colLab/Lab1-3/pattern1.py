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
	print("1")
	i=i+1
