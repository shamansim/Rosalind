library(seqinr)

GCcontent <- function (fichier) {
	sequ=read.fasta(file=fichier)
	
	dataframe=as.data.frame(names(sequ))
	names(dataframe)="nom"

	gccontent=c()
	
	for (n in 1:length(sequ)) {
		compteur=0
		read=unlist(as.matrix(sequ[n]))
		for (t in read) {
			if (t=='g' || t=='c') {compteur=compteur+1}
		}
		gccontent <- c(gccontent,100*(compteur/length(read)))
		
	}
	dataframe=cbind(dataframe,gccontent)
	names(dataframe)[2]='gccontent'
	
	return(dataframe[dataframe$gccontent==max(dataframe$gccontent),])
}
