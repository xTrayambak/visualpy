import random

def random_letters(limit: int):
	letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPZRSTUVWXYZ"
	result = ""
	for x in range(limit):
		result += random.choice(letters)

	return result

def randint(a: int, b: int):
	return random.randint(a, b)

def prng(a, b, c, repeated: int, log: bool):
	currentInt = 0
	operations = [
	"multiply",
	"divide",
	"subtract",
	"add",
	]

	nos = [
	a,
	b, 
	c,
	]

	if log == True:

		# layers of complexity
		for x in range(repeated):
			choosenOperation = random.choice(operations)
			choosenNo1 = random.choice(nos)
			choosenNo2 = random.choice(nos)

			extraInt = random.randint(0, 1)


			if choosenOperation == "multiply":
				if extraInt == random.randint(0, 1):
					print("mult with special")
					currentInt += choosenNo1 * choosenNo2 * x
				else:
					print("mult")
					currentInt += choosenNo1 * choosenNo2
			elif choosenOperation == "divide":
				if extraInt == random.randint(0, 1):
					print("div with special")
					try:
						currentInt += choosenNo1 / choosenNo2 / x
					except ZeroDivisionError:
						print("float zero division error")
						currentInt += choosenNo2 / choosenNo1 * x
				else:
					print("div")
					currentInt += choosenNo1 / choosenNo2
			elif choosenOperation == "subtract":
				if extraInt == random.randint(0, 1):
					print("subtract with special")
					currentInt += choosenNo1 - choosenNo2 + x
				else:
					print("subtract")
					currentInt += choosenNo1 - choosenNo2
			elif choosenOperation == "add":
				if extraInt == random.randint(0, 1):
					print("add with special")
					currentInt += choosenNo1 + choosenNo2 - x
				else:
					print("add")
					currentInt += choosenNo1 + choosenNo2

	elif log == False:

		# layers of complexity
		for x in range(repeated):
			choosenOperation = random.choice(operations)
			choosenNo1 = random.choice(nos)
			choosenNo2 = random.choice(nos)

			extraInt = random.randint(0, 1)


			if choosenOperation == "multiply":
				if extraInt == random.randint(0, 1):
					currentInt += choosenNo1 * choosenNo2 * x
				else:
					currentInt += choosenNo1 * choosenNo2
			elif choosenOperation == "divide":
				if extraInt == random.randint(0, 1):					
					try:
						currentInt += choosenNo1 / choosenNo2 / x
					except ZeroDivisionError:
						currentInt += choosenNo2 / choosenNo1 * x
				else:
					currentInt += choosenNo1 / choosenNo2
			elif choosenOperation == "subtract":
				if extraInt == random.randint(0, 1):
					currentInt += choosenNo1 - choosenNo2 + x
				else:
					currentInt += choosenNo1 - choosenNo2
			elif choosenOperation == "add":
				if extraInt == random.randint(0, 1):
					currentInt += choosenNo1 + choosenNo2 - x
				else:
					currentInt += choosenNo1 + choosenNo2

	else:
		raise TypeError(f"Argument 'log' cannot be anything other than a boolean! It cannot be '{log}'!")
	return int(currentInt) # return raw