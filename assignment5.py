lista = []

print("Toisto keskeytyy kirjoittamalla stop")

while True:

	listaus = input("luo lista: ")

	if listaus == "stop":

		break

	else:

		lista.append(listaus)


uusi_lista = lista[:]



for x in uusi_lista:

	print("Haluatko poistaa mitaan listasta?", lista, "?")

	vastaus = input("(kylla/en): ")

	if vastaus == "en":

		break

	else:

		print("Mita haluat poistaa?")

		poisto = input()

		lista.remove(poisto)

print(lista)
