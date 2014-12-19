def  DNAcount(e):
	f=open(e,'r')
	s=f.readline()
	f.close()
	a=s.count("A")
	c=s.count("C")
	g=s.count("G")
	t=s.count("T")
	print a,c,g,t


