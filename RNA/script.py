def  DNAtoRNA(e):
	f=open(e,'r')
	s=f.readline()
	f.close()
	t=str()
	for i in range(len(s)):
		if s[i]=="T":
			t=t.__add__("U")
		else:
			t=t.__add__(s[i])
	print t


