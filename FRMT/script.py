def main(fichier):
	"""
	"""
	from Bio import Entrez
	from Bio import SeqIO
	Entrez.email = "simon@besson-girard.fr"
	f = open(fichier,'r')
	fline = f.readline().strip()
	l = fline.split(' ')
	listeFasta = ','.join(l)
	handle = Entrez.efetch(db="nucleotide", id=[listeFasta], rettype="fasta")
	records = list (SeqIO.parse(handle, "fasta"))
	compteur = 0
	for j in range(len(records)):
		if len(records[j].seq)<=len(records[compteur].seq):
			compteur = j

	print(records[compteur].format("fasta"))
