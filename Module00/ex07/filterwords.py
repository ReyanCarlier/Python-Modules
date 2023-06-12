import sys
import re

def main():
    if (len(sys.argv) != 3):
        print("ERROR")
        return None
    try:
        size = int(sys.argv[2])
        list_words = re.findall(r"[\w]+", sys.argv[1])
        if (len(list_words) == 0):
            print("ERROR")
        else:
            good_words = []
            for word in list_words:
                if (len(word) > size):
                    good_words.append(word)
            print(good_words)
    except ValueError:
        print("ERROR")

if (__name__ == "__main__"):
	main()