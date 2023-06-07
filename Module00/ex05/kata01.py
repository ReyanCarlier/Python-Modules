kata = {
	'Python': 'Guido van Rossum',
	'Ruby': 'Yukihiro Matsumoto',
	'PHP': 'Rasmus Lerdorf',
}

def main():
    for key, val in kata.items():
        print(key, "was created by", val)

if (__name__ == "__main__"):
    main()