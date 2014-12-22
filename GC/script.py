def gc(fasta_file):
	"""
		compute the GC content of a fasta file and return the name 
		and the GC percentage of the richest read
	"""
	f=open(fasta_file,'r')
	fline=f.readline()
	dico={}
	while fline:
		fline=fline[:-1]
		compteurGC=0
		fline2=f.readline()
		fline2=fline2[:-1]
		longueur=len(fline2)
		for l in fline2:
			if l=='G' or l=='C':
				compteurGC+=1
		GCcontent=compteurGC/longueur
		dico[fline]=GCcontent
	return dico
