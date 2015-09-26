def main(fichier):
	"""
		gives back even-numbered lines
	"""
	f = open(fichier,'r')
	compteur = 1
	fline = f.readline()
	g = open('output.txt','w')
	while fline:
		if compteur%2==0:
			g.write(fline)
		compteur+=1
		fline = f.readline()
	f.close()
	g.close()
