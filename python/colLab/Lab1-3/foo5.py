n=4
i=1
j=1
k=1
while i<=n:
	j=1
	while j<=4:
		if i==j:
			print(k , end=" ")
			k=k+2
		else:
			print("0" , end=" ")
		j=j+1
	i=i+1
	print()
