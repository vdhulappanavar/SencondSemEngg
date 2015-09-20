para=input("Eneter a paragraph:")
d={}
for word in para.split():
	word1=word.lower()
	if word1[0] not in d:
		d[word[0]]=[]
	d[word1[0]].append(word)
print(d)
for i in d:
	print(i,":")
	d[i].sort()
	for j in d[i]:
		print("\t",j)


