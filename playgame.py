from random import randint


class playGame:
    def __init__(self, maxVal):
        self.randomNumber = 0
        self.maxGuess = 5
        self.maxVal = maxVal
        self.generateNumber()

    def generateNumber(self):
        self.randomNumber = randint(1, self.maxVal)

    def play(self):
        while self.maxGuess > 0:
            try:
                guess = int(input(f"Guess  Number 1 to {self.maxVal}: "))
                if self.randomNumber == guess:
                    print(f"You have correctly guessed the number!!! {self.randomNumber}")
                    break
                else:
                    print("Incorrect guess, try again.")
                    self.maxGuess -= 1
            except ValueError:
                print("Incorrect input")
        self.reset()

    def reset(self):
        choice = input("play again ? Y or N: ")
        if choice.lower() == 'y':
            self.generateNumber()
            self.maxGuess = 5
            self.play()
