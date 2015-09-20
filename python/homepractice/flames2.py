#print('hello')
n1=input('enter first name: ')
n2=input('enter second name: ')
#efflen=len(set(n1)^set(n2))
#print(efflen)
n3=list(n1)
n4=list(n2)
s=set(n1+n2)
for i in s:
    if i in n3 and i in n4:
        n3.remove(i)
        n4.remove(i)
efflen=len(n3)+len(n4)
print(efflen)
f=['f', 'l', 'a', 'm', 'e', 's']
l=len(f)
r=efflen%l
pr=0
print("Hello World")
if pr:
	print("True")
else:
	print("False")
while not l==1:
    try:
		#if 0:
		#	pass
        print("inside:",f[r-pr-1],"r=", r, " ","pr=",pr,"pr-r-1=", r-pr-1)
        del f[r-pr-1]
    except:
        print(f[r-1],"r=", r, " ","pr=",pr,"pr-r-1=", r-pr-1)
        del f[r-1]
    l=len(f)
    pr=r
    r=efflen%l
    print("outside" , "len=",l , "r=", r, " ","pr=",pr,"pr-r-2=", r-pr-1)
print(f)