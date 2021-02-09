try:
	a = int(input("Anna luku: "))
	if a <= 2:
		b = a
	print("b = ", b)
except NameError:
	print("NameError")
