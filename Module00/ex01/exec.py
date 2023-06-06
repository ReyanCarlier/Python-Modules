# Make a program that takes a string as argument, reverses it, swaps its letters case and print the result.
# • If more than one argument are provided, merge them into a single string with each argument separated by a space character.
# • If no argument are provided, do nothing or print an usage.

import sys;

def main():
	if (len(sys.argv) < 2):
		print("Invalid number of arguments. Usage : python3 exec.py [\"argv1\"] <\"argv2\"> ...")
	else:
		argv_index = len(sys.argv) - 1
		result = ""
		while (argv_index > 0):
			str_index = len(sys.argv[argv_index]) - 1
			while (str_index >= 0):
				if (sys.argv[argv_index][str_index].islower()):
					result += sys.argv[argv_index][str_index].capitalize()
				elif (sys.argv[argv_index][str_index].isupper()):
					result += sys.argv[argv_index][str_index].lower()
				else:
					result += sys.argv[argv_index][str_index]
				str_index-=1
			argv_index-=1
			if (argv_index > 0):
					result += " "
		print(result)

# Alternative way using slices :

# def main():
# 	if (len(sys.argv) < 2):
# 		print("Invalid number of arguments. Usage : python3 exec.py [\"argv1\"] <\"argv2\"> ...")
# 	else:
# 		result = ""
# 		for string in reversed(sys.argv[1:]): #Skip argv[0], loop in reverse order
# 			if result != "":
# 				result += " "
# 			string = string[::-1] #Reverse the string
# 			for char in string:
# 				if char.islower():
# 					result += char.capitalize()
# 				elif char.isupper():
# 					result += char.lower()
# 				else:
# 					result += char
# 		print(result)

if __name__ == "__main__":
	main()