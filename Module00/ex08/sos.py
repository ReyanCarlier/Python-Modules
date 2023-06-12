import sys

MORSE_CODE_DICT = {
    'A':'.-', 'B':'-...',
	'C':'-.-.', 'D':'-..', 'E':'.',
	'F':'..-.', 'G':'--.', 'H':'....',
	'I':'..', 'J':'.---', 'K':'-.-',
	'L':'.-..', 'M':'--', 'N':'-.',
	'O':'---', 'P':'.--.', 'Q':'--.-',
	'R':'.-.', 'S':'...', 'T':'-',
	'U':'..-', 'V':'...-', 'W':'.--',
	'X':'-..-', 'Y':'-.--', 'Z':'--..',
	'1':'.----', '2':'..---', '3':'...--',
	'4':'....-', '5':'.....', '6':'-....',
	'7':'--...', '8':'---..', '9':'----.',
	'0':'-----', ', ':'--..--', '.':'.-.-.-',
	'?':'..--..', '-':'-....-',
	'(':'-.--.', ')':'-.--.-'
}

def main():
    if (len(sys.argv) == 1):
        print("Usage : python3 sos.py [string1] <string2> <string3> ...")
        return None
    curated_argv = []
    for i in range(len(sys.argv)):
        if (i == 0):
            continue
        curated_argv.append(sys.argv[i])
    result = ""
    for i in range(len(curated_argv)):
        for char in curated_argv[i]:
            if (char.isdigit()):
                char = str(char)
            elif (char.islower()):
                char = char.upper()
            elif (char.isspace()):
                result += "/ "
                continue
            try:
                result += MORSE_CODE_DICT[char]
            except:
                print("ERROR")
                return
            result += " "
        if (i < len(curated_argv) - 1):
            result += "/ "
    print(result)

if (__name__ == "__main__"):
    main()