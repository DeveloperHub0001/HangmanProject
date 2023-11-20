import WordGenerator as wg
import os


def playGame():
    state = 0
    didPlayerWin = False
    game_running = True
    wordToGuess = wg.getWord()
    gameBoard = [
        "      Hang Man  ",
        "____________________",
        "|                   |",
        "|        _______    |",
        "|       |       |   |",
        "|               |   |",
        "|               |   |",
        "|               |   |",
        "|               |   |",
        "|               |   |",
        "|               |   |",
        "|_______________|___|",
    ]
    displayStr = "-" * len(wordToGuess.word)
    guessed_letters = set()
    while game_running:
        os.system("cls")  # 'clear' for mac and unix
        printBoard(gameBoard)
        print(displayStr + "      Hint: " + wordToGuess.hint)
        print("Guessed Letters: ", guessed_letters)
        if displayStr == wordToGuess.word.lower():
            print("The word was " + wordToGuess.word)
            didPlayerWin = True
            break
        if state == 6:
            print("The word was " + wordToGuess.word)
            break
        guess = input("Guess a letter: ")
        actualGuess = guess[0].lower()
        guessed_letters.add(actualGuess)
        if checkGuess(actualGuess, wordToGuess.word):
            displayStr = updateDisplayWord(wordToGuess.word, actualGuess, displayStr)
        else:
            state += 1
            gameBoard = updateBoard(gameBoard, state)

    return didPlayerWin


def printBoard(board):
    for i in board:
        print(i)


def checkGuess(guess, word):
    for i in word:
        if i.lower() == guess:
            return True
    return False


def updateDisplayWord(word, guess, display):
    newDisplayWord = ""
    for i in range(len(word)):
        if word[i].lower() != guess:
            newDisplayWord += display[i] if display[i] != "-" else "-"
        else:
            newDisplayWord += guess
    return newDisplayWord


def updateBoard(board, state):
    if state == 1:
        board[5] = "|       O       |   |"
    elif state == 2:
        board[6] = "|       |       |   |"
        board[7] = "|       |       |   |"
    elif state == 3:
        board[6] = "|      /|       |   |"
    elif state == 4:
        board[6] = "|      /|\\      |   |"
    elif state == 5:
        board[8] = "|      /        |   |"
    elif state == 6:
        board[8] = "|      / \\      |   |"
    return board
