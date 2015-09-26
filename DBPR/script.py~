def main(fichier):
	"""
		navigate into protein database
	"""
	f = open(fichier,'r')
	fline = f.readline().strip()
	from Bio import ExPASy
	from Bio import SwissProt
	handle = ExPASy.get_sprot_raw(fline)
	record = SwissProt.read(handle)
	go = []
	for i in record.cross_references:
		if i[0] == 'GO' and i[2][0]=='P':
		        go.append(i[2].lstrip('P:'))
	print '\n'.join(go)
