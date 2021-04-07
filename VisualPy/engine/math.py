from fractions import Fraction
import random
import letters
import math



class mathf:
	def random(self, limit: int):
		return random.randint(0, limit)

	def rng(self, inputList):
		a, b, c = inputList
		
		return letters.prng(a=a, b=b, c=c, repeated=a*b*c, log=False)

	def floor(self,a):
		"""
		Returns the floor of `a` as an integral.
		"""
		return math.floor(x=a)

	def sin(self,a):
		"""
		Returns the sine of `a`.
		"""
		return math.sin(x=a)

	def nan(self):
		"""
		Returns `nan`, a floating point "not a number"
		"""
		return float("nan")

	def inf(self):
		"""
		Returns a floating point infinity number. Equivalent of float('inf')
		"""
		return float('inf')
	
	def asin(self,a):
		"""
		Returns the arc sine of `a`.
		"""
		return math.asin(x=a)

	def add(a: int, b: int):
		return a + b
	def subtract(a: int, b: int):
		return a - b
	def multiply(a: int, b: int):
		return a * b
	def divide(a: int, b: int):
		return a / b
	def cos(a):
		"""
		Description:\n
		Returns the hyperbolic cosine of the value `a` inputted.\n
		Parameters:\n
        `a` - The value\n
		"""
		return math.acos(a)

print(mathf.cos(a=30))