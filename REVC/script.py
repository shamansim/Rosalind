def  complement(e):
	f=open(e,'r')
	s=f.readline()
	f.close()
	t=str()
	i=len(s)-1
	while i >= 0:
		if s[i]=="A" and i>=0:
			t=t.__add__("T")
		if s[i]=="T" and i>=0:
			t=t.__add__("A")
		if s[i]=="C" and i>=0:
			t=t.__add__("G")
		if s[i]=="G" and i>=0:
			t=t.__add__("C")
		i=i-1
	print t


