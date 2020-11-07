import playgame

if __name__ == '__main__':
    try:
        maxVal = int(input("Enter the maximum number: "))
        game = playgame.playGame(maxVal)
        game.play()
    except ValueError as e:
        print("Invalid input")
