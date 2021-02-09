def pyramiidi(n):

	k = 2*n - 2


	for i in range(0, n):

		for j in range(0, k):

			print(end=" ")

		k = k - 1

		for j in range(0, i+2):
			print("A", end="")

		for j in range(0, i+1-1):

			print("A", end="")

		print("\r")

n = 10
pyramiidi(n)
