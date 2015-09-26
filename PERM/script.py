import itertools as itt
def perm(fichier):
	f=open(fichier,'r')
	g=open("output.txt",'w')
	fline=f.readline
	fline=int(fline)
	objet=itt.permutations()
