import random
pointlist=[]
def gen_point(ll , ul):
	return random.randint(ll , ul)

def gen_points():
	n=int(input("how many number of points do you want to generate? : "))
	for i in range(0,n):
		ll=int(input("Enter Lower Limit for genration of points: "))
		ul=int(input("Enter Upper Limit for genration of points: "))
		pointlist.append((gen_point(ll , ul) , gen_point(ll , ul)))
		print()

def dist( p1 , p2):
	return ((p2[0]-p1[0])**(2)+(p2[1]-p1[1])**(2))**(0.5)

def nearerxy():
	nearx=pointlist[0][0]
	neary=pointlist[0][1]
	pos=0
	for i in range(1 , len(pointlist)):
		if pointlist[i][0]<nearx and pointlist[i][1]<neary:
			nearx=pointlist[i][0]
			neary=pointlist[i][1]
			pos=i
	print("The point nearest to the orgin wrt xy is: " , pointlist[pos] )

def nearerdist():
	neard=dist((0,0) , pointlist[0])
	pos=0
	for i in range(1 , len(pointlist)):
		if dist((0,0) , pointlist[i])<neard:
			neard=dist((0,0) , pointlist[i])
			pos=i		
	print("The point nearest to the orgin wrt dist is: " , pointlist[pos] )

def listdist():
	distance=[]
	for i in pointlist:
		distance.appned(dist((0,0) , i))
	print("The distance list: " , d)
	print()

def sort():
	for i in range(len(pointlist)-1 , 0 , -1):
		for j in range(0 , i):
			if dist((0,0) , pointlist[j])>dist((0,0) , pointlist[j+1]):
				pointlist[j] , pointlist[j+1] = pointlist[j+1] , pointlist[j]
	print()	
	print("Sorted List:" , pointlist)
	print()

def main():
	gen_points()
	print(pointlist)
	print()
	print("Enter the index of the points you want to find the distance between:( 1-",len(pointlist),")")
	print()
	i1=int(input("Enter index of point 1:"))-1
	i2=int(input("Enter index of point 2:"))-1
	print("Distance between", pointlist[i1] , pointlist[i2] , "is:" , dist(pointlist[i1] , pointlist[i2]))
	print()
	nearerxy()
	print()
	nearerdist()
	print()
	sort()
	print()

main()
print("**********************************")
