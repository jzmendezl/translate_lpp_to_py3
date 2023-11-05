import sys
import numpy as np

def main():
	_ = 0
	__ = 0
	___ = 0
	my_real = 0.0
	_real2 = 0.0
	__result_real__ = 0.0

	def add(n1,n2):
		result = 0
		result = n1 + n2
		return result



	def mult(r1,r2):
		the__real_one = 0.0
		the__real_one = r1 + r2
		return the__real_one



	def greeting():
		sayhello = ""
		sayhello = "Hi folks :) "
		print(sayhello, end="", sep="")



	def introducemyself():
		return "I'm a student"


	_ = 20
	_real2 = -9.5
	__ = 7
	my_real = 2.7
	___ = add(_,__)
	__result_real__ = mult(my_real,_real2)
	print(("The result of adding "),_," and ",__," is: ",___, end="", sep="")
	print()

	print(("The result of multiplyin" + "g "),my_real," a",'n',"d ",_real2," is: ",__result_real__, end="", sep="")
	print()

	print()

	greeting()
	print(introducemyself()," that loves how to learn :3", end="", sep="")


if __name__ == "__main__":
	main()
