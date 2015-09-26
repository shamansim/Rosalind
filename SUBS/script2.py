def main(fichier):
	"""
		find a motif t into a string s
	"""
	f = open(fichier,'r')
	s = f.readline().strip()
	t = f.readline().strip()
	
	position = 0
	location = s.find(t,position)
	while location!=-1:
		print(str(location+1))
		position = location+1
		location = s.find(t,position)
		
	
