# Make a program that takes a number as argument, checks whether it is odd, even or zero, and print the result.
# • If more than one argument are provided or if the argument is not an integer, print an error message.
# • If no argument are provided, do nothing or print an usage.

import sys

def main():
	if (len(sys.argv) != 2):
		print("Invalid number of arguments. Usage : python3 whois.py <number>")
	else:
		try:
			x = int(sys.argv[1])
			if (x == 0):
				print("I'm Zero.")
			elif (x % 2 == 0):
				print("I'm Even.")
			else:
				print("I'm Odd.")
		except ValueError:
			print("Argument isn't a valid number.")

if (__name__ == "__main__"):
	main()