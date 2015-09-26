def main(chiffre):
	"""
		gives the chiffre-ieme number of the Fib numbers
	"""
	if chiffre==0:
		return 0
	elif chiffre ==1:
		return 1
	else:
		return main(chiffre-1)+main(chiffre-2)
		
		
		
