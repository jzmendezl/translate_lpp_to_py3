import sys
import numpy as np

def main():
	rows = 0
	coef = 0
	space = 0
	i = 0
	j = 0
	rows = 8
	for i in range(0, rows + 1 + 1):
		for space in range(1, rows - i + 4 + 1):
			print(" ", end="", sep="")
		for j in range(0, i + 1):
			if (j  ==  0)  or  (i  ==  0):
				coef = 1
			else:
				coef = coef * (i - j + 1) / j
			print(coef, end="", sep="")
			print("   ", end="", sep="")
		print()



if __name__ == "__main__":
	main()
