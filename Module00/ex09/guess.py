import random

def main():
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!")
    print("")

    counter = 0
    secret_number = random.randint(1, 99)
    while (True):
        counter += 1
        print("What's your guess between 1 and 99 ?")
        guess = input(">> ")
        try:
            if (guess == "exit"):
                break
            guess = int(guess)
            if (guess > 99 or guess < 1):
                print("Your guess must be between 1 and 99!")
            else:
                if (guess == secret_number):
                    if (secret_number == 42):
                        print("The answer is the ultimate question of life, the universe and everything is 42.")
                    if (counter == 1):
                        print("Congratulations! You got it on your first try!")
                        break
                    else:
                        print("You won in", counter, "attempts!")
                        break
                elif (guess < secret_number):
                    print("Too low !")
                else:
                    print("Too high !")
        except:
            print("That's not a number.")
    print("Goodbye !")

if (__name__ == "__main__"):
    main()