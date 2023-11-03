import sys
import numpy as np

def main():
	# Declaración de matriz en Python
	o_o = np.empty((5, 10, 5, 5, 3, 3, 3), dtype=int)
	booleans = np.empty((2,2,2), dtype=bool)
	walker1 = 0
	walker2 = 0
	walker3 = 0
	result = False
	o_o[0][2][1][3][1][2][0] = 19
	print("the secret number is: ", o_o[0][2][1][3][1][2][0])
	print()

	print("what about the other array?", "let´s make it possible ", ':', 'v')
	print()

	booleans[0][0][0] = False
	booleans[0][0][1] = False
	booleans[0][1][0] = True
	booleans[0][1][1] = True
	booleans[1][0][0] = False
	booleans[1][0][1] = False
	booleans[1][1][0] = True
	booleans[1][1][1] = False
	walker1 = 0
	while walker1 < 2:
		walker2 = 0
		while walker2 < 2:
			walker3 = 0
			while walker3 < 2:
				print("booleans[", walker1, ",", walker2, ",", walker3, "] has value: ", booleans[walker1][walker2][walker3])
				print()

				walker3 = walker3 + 1
				walker2 = walker2 + 1
				walker1 = walker1 + 1
				print()

				print("end of the program :3 ", 45 * 98 / 23  //  2  **  3)


if __name__ == "__main__":
	main()