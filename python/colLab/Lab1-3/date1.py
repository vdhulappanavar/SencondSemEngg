import sys

days=[[0,31,28,31,30,31,30,31,31,30,31,30,31],[0,31,29,31,30,31,30,31,31,30,31,30,31]]
date=input("Enter date in dd-mm-yyyy form:")
(dd , mm , yy)=date.split("-")
dd=int(dd)
mm=int(mm)
yy=int(yy)
leap=0
def nextDate():
	ndd=dd;nmm=mm;nyy=yy;
	#print("Leap:",leap)
	#print("Calculating next date")
	if(mm==12 and days[leap][mm]==dd):
		nyy+=1
		ndd=1
		nmm=1
	#print(mm)
	elif days[leap][mm]==dd:
		nmm+=1
		ndd=1
	else:
		ndd+=1
	print("Next Date:" ,ndd,"-",nmm,"-",nyy)
	
valid=0

if 1<= mm <= 12:
	if(yy%4==0 and yy%100!=0 or yy%400==0):
		leap=1
		#print("leap")
	if 1<= dd <= days[leap][mm]:
		#print("Valid")
		nextDate()
	else:
		print("Inavlid")
		sys.exit(1)
else:
	print("Inalid date")
	sys.exit(1)


