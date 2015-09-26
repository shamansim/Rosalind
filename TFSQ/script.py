def main(fichier):
	"""
		convert fastq into fasta
	"""
	from Bio import SeqIO
	handle = open(fichier, "r")
	g = open('output.txt','w')
	SeqIO.convert(handle, 'fastq', g, 'fasta' )
	handle.close()
	g.close()
