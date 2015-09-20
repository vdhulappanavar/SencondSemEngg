
rhyme="""
Old MacDonald had a farm, E I E I O, 
And on his farm he had a animal, E I E I O. 
With a soundsound here and a soundsound there, 
Here a sound, there a sound, everywhere a soundsound. 
Old MacDonald had a farm, E I E I O. 
"""
#def print_rhyme(l):
#	print(l)

def printsep(mlen):
	for i in range(0 , mlen):
		print("-",end='')
	print()


def sep1(rhyme1):
	l=rhyme1.split('\n')
	mlen=len(l[0])

	for i in l:
		#print(i)
		if len(i)>mlen:
			mlen=len(i)
		#print(len(i))
	return mlen

def replace1(d={'dog':'woof'}):
	#d={}
	#print(d)
	rhyme1=rhyme
	for i in d:
		if not d[i]==None:		
			rhyme1=rhyme1.replace('animal,' , i)
			rhyme1=rhyme1.replace('soundsound' , d[i]+d[i])
			rhyme1=rhyme1.replace('sound' , d[i])
		print(rhyme1)
		printsep(sep1(rhyme1))


		





replace1()
printsep(mlen)
replace1(d={"cow":"mooo"})
print()
printsep(mlen)
print()
replace1(d={"cow":"mooo" , "pig":"oink"})
printsep(mlen)
#print(sep1())
"""print()
print("print_rhyme:")
print_rhyme(1,2,3)
"""
