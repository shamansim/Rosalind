def main(fichier):
	"""
		compute molecular weight of a protein sequence
	"""
	from Bio.SeqUtils import *
	f = open(fichier,'r')
	fline = f.readline()
	print("%0.3f" % molecular_weight(fline[:-1], "protein"))
	f.close()
