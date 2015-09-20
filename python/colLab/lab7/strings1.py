def foo(l , sep="," , firstString='result:'):
	#print("l1=",l)
	l=list(l)
	#print("l2=",l)
	l.insert(0 , firstString)
	#print("l3=",l)	
	print(sep.join(l))
	
	
#foo(["Hello" , "Hi"] , sep='!')
n=int(input("Enter the number of Strings you want to enter: "))
l=[]
s=''
ss=''
for i in range(0 , n):
	l.append(input("Enter a string: "))
if input("Enter yes if you want to enter a seperator: ") == 'yes':
	s=input("Enter a seperator: ")		
if input("Enter yes if you want to enter a Start String: ") == 'yes':
	ss=input("Enter a Start String: ")		
if s and ss:
	foo(l , sep=s , firstString=ss)
elif s:
	foo(l , sep=s )
elif ss:
	foo(l , firstString=ss)
else:
	foo(l)
