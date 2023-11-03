import sys
import numpy as np

def main():
	_ = 0
	__ = 0
	___ = 0
	my_real = 0.0
	_real2 = 0.0
	__result_REAL__ = 0.0

	def add(n1, n2):
		result = 0
		result = n1 + n2
		return result



	def mult(r1, r2):
		the__real_one = 0.0
		the__real_one = r1 + r2
		return the__real_one


	sayHello = ""
	sayhello = "hi folks :) "
	print(sayhello)

	def introducemyself():
		return "i'm a student"


	_ = 20
	_real2 = 9.5
	__ = 7
	my_real = 2.7
	___ = add(_, __)
	__result_real__ = mult(my_real, _real2)
	print("the result of adding ", _, " and ", __, " is: ", ___)
	print()

	print("the result of multiplyin" + "g ", my_real, " a", 'n', "d ", _real2, " is: ", __result_real__)
	print()

	print()


	print(introducemyself(), " that loves how to learn :3")


if __name__ == "__main__":
		main()