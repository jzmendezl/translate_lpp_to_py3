import sys
import numpy as np

def main():
	acumulador = 0
	i = 0
	i = 0
	acumulador = 0
	while True:
		print(("Valor del acumulador en la iteracion: "),(acumulador), end="", sep="")
		print()

		i = i + 1
		acumulador = acumulador + (i * 2)
		if ((i  ==  20)  or  (acumulador  %  5  ==  4)):
			break


if __name__ == "__main__":
	main()