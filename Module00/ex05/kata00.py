kata = (19,42,21)

def main():
    result = "The " + str(len(kata)) + " numbers are: "
    for i in range(0, len(kata)):
        result += str(kata[i])
        if (i != len(kata) - 1):
            result += ", "
    print(result)

if (__name__ == "__main__"):
    main()