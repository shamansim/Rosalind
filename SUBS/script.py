def to_str(a):
    """
    	pour afficher le resultat final dans le bon format
    """
    l=str()
    for i in a: 
  	l=l.__add__(str(i)+'\ ')
    return l

def compare(s,t,r,parcouru):
	print 'je prends en entree s :'+s+' r :'+str(r)+' parcouru :'+str(parcouru)#
	try:
		indexs=s.index(t)
	except ValueError:
		return None
	
	#pour normaliser par rapport aux autres parcours
	parcouru=indexs+parcouru
	print 'indexs vaut :'+str(indexs)#
	print 'parcouru vaut :'+str(parcouru)#
	print 'parcouru+indexs vaut :'+str(parcouru+indexs)#
	r.append(parcouru)
	compare(s[parcouru+1:],t,r,parcouru)
	
def subs(e):
	f=open(e,'r')
	s=f.readline()
	t=f.readline()
	f.close()	
# 1-redefinition de t et s a cause du \n
	t=t[:-1]
	s=s[:-1]
# 2-comparaison de tous les s segmentes par rapport a t
	r=list()
	g=open("resultat.txt",'w')
	compare(s,t,r,0)
	l=to_str(r)
	print(l)
	g.write(l)
	g.close()

