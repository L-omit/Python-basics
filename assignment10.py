def reverse(x):
	x = x[::-1] # alku ja loppuarvoja ei ole maaritelty ja koska luku on negatiivinen niin komento ::-1 tulostaa koko listan mutta menee yksi kerrallaan takaperin
	return x
x = reverse([1,2,3,4,5])
print(x)
