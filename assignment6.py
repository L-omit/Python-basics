def compareNumbers(luku1, luku2):
	if luku1 > luku2:
		return luku1;
	elif luku1 == luku2:
		print("sama luku")
	else:
		return luku2;
luku1 = int(input("Anna luku: "))
luku2 = int(input("Anna toinen luku: "))
print("Suurempi luku on: {}".format(compareNumbers(luku1, luku2)))
input("PRESS ENTER TO CONTINUE")

