import random

def drawHangMan(numOfTries):

    if numOfTries == 5:
        print(
            "----|  \n"
            "|   0  \n"
            "|      \n"
            "|      \n"
            "------ \n"
        )

    elif numOfTries == 4:
        print(
            "----|  \n"
            "|   0  \n"
            "|   |  \n"
            "|      \n"
            "------ \n"
        )

    elif numOfTries == 3:
        print(
            "----|  \n"
            "|   0  \n"
            "|   |\ \n"
            "|      \n"
            "------ \n"
        )

    elif numOfTries == 2:
        print(
            "----|  \n"
            "|   0  \n"
            "|  /|\ \n"
            "|      \n"
            "------ \n"
        )

    elif numOfTries == 1:
        print(
            "----|  \n"
            "|   0  \n"
            "|  /|\ \n"
            "|    \ \n"
            "------ \n"
        )

    elif numOfTries == 0:
        print(
            "----|  \n"
            "|   0  \n"
            "|  /|\ \n"
            "|  / \ \n"
            "------ \n"
        )

def Tiger():

    blankSpaces = ["_", "_", "_", "_", "_"]

    for x in blankSpaces:
        print(x)

    # Head, body, 2 arms and 2 legs
    numOfTries = 6

    while numOfTries > 0:

        if (blankSpaces[0] == "T" and blankSpaces[1] == "i"
                and blankSpaces[2] == "g" and blankSpaces[3] == "e" and blankSpaces[4] == "r"):
            print("YOU WON THE GAME!")
            exit()

        userInput = input("Enter a letter: ")

        if (userInput == "T" or userInput == "t"):
            blankSpaces[0] = "T"

            for x in blankSpaces:
                print(x)

        elif (userInput == "i" or userInput == "I"):
            blankSpaces[1] = "i"

            for x in blankSpaces:
                print(x)

        elif (userInput == "g" or userInput == "G"):
            blankSpaces[2] = "g"

            for x in blankSpaces:
                print(x)

        elif (userInput == "e" or userInput == "E"):
            blankSpaces[3] = "e"

            for x in blankSpaces:
                print(x)

        elif (userInput == "r" or userInput == "R"):
            blankSpaces[4] = "r"

            for x in blankSpaces:
                print(x)

        else:

            numOfTries = numOfTries - 1

            drawHangMan(numOfTries)

    print("You lost the game!")


def Dog():
    blankSpaces = ["_", "_", "_"]

    for x in blankSpaces:
        print(x)

    # Head, body, 2 arms and 2 legs
    numOfTries = 6

    while numOfTries > 0:

        if (blankSpaces[0] == "D" and blankSpaces[1] == "o"
                and blankSpaces[2] == "g"):
            print("YOU WON THE GAME!")
            exit()

        userInput = input("Enter a letter: ")

        if (userInput == "D" or userInput == "d"):
            blankSpaces[0] = "D"

            for x in blankSpaces:
                print(x)

        elif (userInput == "o" or userInput == "O"):
            blankSpaces[1] = "o"

            for x in blankSpaces:
                print(x)

        elif (userInput == "g" or userInput == "G"):
            blankSpaces[2] = "g"

            for x in blankSpaces:
                print(x)

        else:
            numOfTries = numOfTries - 1

            drawHangMan(numOfTries)

    print("You lost the game!")


def main():
    print("Welcome to the Hangman Game!")

    guessWords = ["Tiger", "Dog"]

    indexNum = random.randint(0, 1)

    if indexNum == 0:
        Tiger()

    elif indexNum == 1:
        Dog()

main()
