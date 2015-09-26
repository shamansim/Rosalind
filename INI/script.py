def main(fichier):
	"""
		count a t c g in a sequence using Bio.Seq
	"""
	f = open(fichier,'r')
	fline = f.readline().strip()
	from Bio.Seq import Seq
	my_seq = fline
	print(str(my_seq.count("A"))+" "+str(my_seq.count("C"))+" "+str(my_seq.count("G"))+" "+str(my_seq.count("T")))
	f.close()
	
