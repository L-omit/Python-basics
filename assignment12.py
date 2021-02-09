def vowels(asd):
	vokaalit = 0
	for char in asd:
		if char in "aeiou":
			vokaalit = vokaalit+1
	return vokaalit
print(vowels(input("Sano jotain: ")))
