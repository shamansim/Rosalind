def main(fichier):
	"""
		gives back the count of words
	"""
	f = open(fichier,'r')
	fline = f.readline()
	fline = fline[:-1]
	d = dict()
	for i in fline.split(' '):
		if d.has_key(i):
			d[i]+=1
		else:
			d[i]=1
	g = open ('output.txt','w')
	for key, value in d.items():
		g.write(str(key)+' '+str(value)+'\n')
	f.close()
	g.close()
