def main(fichier):
	"""
		translate RNA into protein
	"""
	from Bio.Seq import Seq
	f = open(fichier,'r')
	g = open('output.txt','w')
	fline = f.readline()
	my_seq = Seq(fline[:-1])
	g.write(str(my_seq.translate(to_stop=True)))
	f.close()
	g.close()
