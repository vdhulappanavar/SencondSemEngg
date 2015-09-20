LowerLimit=int(input("LowerLimit:"))
UpperLimit=int(input("UpperLimit:"))
i=LowerLimit
while i<=UpperLimit:
	if i<10:
		print(i,end=' ')
	elif i>99 and i<1000:
		copy=i
		sum=0
		while copy!= 0:
			digit=copy%10
			sum=sum+(digit*digit*digit)
			copy=copy//10
		if sum==i:
			print(i ,  end=' ')
	
	i=i+1
print()
