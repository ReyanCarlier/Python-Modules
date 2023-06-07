kata = (2019, 9, 25, 3, 30)

def main():
    string = ""
    string += '{:02d}'.format(kata[1]) + "/"
    string += '{:02d}'.format(kata[2]) + "/"
    string += '{:04d}'.format(kata[0]) + " "
    string += '{:02d}'.format(kata[3]) + ":"
    string += '{:02d}'.format(kata[4])
    print(string)

if (__name__ == "__main__"):
    main()