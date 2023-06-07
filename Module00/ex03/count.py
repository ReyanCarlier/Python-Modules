# Part 1. text_analyzer
# Create a function called text_analyzer that takes a single string argument and displays the sums of its upper-case characters, lower-case characters, punctuation characters and spaces.
# • If None or nothing is provided, the user is prompted to provide a string.
# • If the argument is not a string, print an error message.
# • This function must have a docstring explaning its behavior.
# Test your function with the python console

# Part 2. __name__==__main__
# In the previous part, you wrote a function that can be used in the console or in another file when imported. Without changing this behavior, update your file so it can also be launched as a standalone program.
# • If more than one argument is provided to the program, print an error message.
# • Otherwise, use the text_analyzer function.

import sys

def printf(format, *values):
	print(format % values)

def text_analyzer(string=None):
	'''Takes a single string argument and displays the sums of its upper-case characters, lower-case characters, punctuation characters and spaces. If no string is given in arguments, asks the user an input.'''
	if (string == None):
		try:
			string = input("Provide a string : ")
		except:
			print("Invalid argument, must provide a string.")
			return None
	else:
		try:
			test = int(string)
			print("Invalid argument, must provide a string.")
			return None
		except:
			None
	upperletters = 0
	punctuation = 0
	lowerletters = 0
	spaces = 0
	for char in string:
		if char.isspace():
			spaces+=1
		elif char.isupper():
			upperletters+=1
		elif char.islower():
			lowerletters+=1
		elif char.isdigit():
			continue
		else:
			punctuation+=1
	printf("The text contains %d character(s):", len(string))
	printf("- %d upper letter(s)", upperletters)
	printf("- %d lower letter(s)", lowerletters)
	printf("- %d punctuation mark(s)", punctuation)
	printf("- %d space(s)", spaces)

def main():
	if (len(sys.argv) > 2):
		print("Invalid arguments. Usage : python3 count.py <string>")
	elif (len(sys.argv) == 2):
		text_analyzer(sys.argv[1])
	else:
		text_analyzer(None)

if __name__ == "__main__":
	main()