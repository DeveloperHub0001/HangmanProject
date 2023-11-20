import GameScript


running = True

while running:
    print("1: Play Game\n2: Quit")
    selection = input("Enter Selection: ")
    if selection == "1":
        results = GameScript.playGame()
        if results:
            print("great job")
        else:
            print("better luck next time")
    elif selection == "2":
        running = False
    else:
        print("invalid input")
    print("")
