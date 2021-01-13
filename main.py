import random

scoreWin = 0
scoreLose = 0
while True:

    validPlays = ["Rock", "Paper", "Scissors"]
    opt = input("Press (R) for Rock, (P) for Paper, (S) to Scissors, (1) to see your Score or (0) to Exit the program: ")
    oponent = random.choice(validPlays)

    if(opt == '0'):
        print("Exiting...")
        exit(0)

    elif opt in ("r", "R"):
        print("You chose Rock.")
        print("Your Opponent rolled " + opponent + ".")
        if(opponent == "Rock"):
            print("It's a Tie!")

        elif(opponent == "Paper"):
            print("You lost! :( ")
            scoreLose += 1
        
        elif(opponent == "Scissors"):
            print("You won! :) ")
            scoreWin += 1
        
    elif opt in ("p", "P"):
        print("You chose Paper.")
        print("Your Opponent rolled " + opponent + ".")
        if(opponent == "Paper"):
            print("It's a Tie!")

        elif(opponent == "Scissors"):
            print("You lost! :( ")
            scoreLose += 1
        
        elif(opponent == "Rock"):
            print("You won! :) ")
            scoreWin += 1

    elif opt in ("s", "S"):
        print("You chose Scissors.")
        print("Your Opponent rolled " + opponent + ".")
        if(opponent == "Scissors"):
            print("It's a Tie!")

        elif(opponent == "Rock"):
            print("You lost! :( ")
            scoreLose += 1
        
        elif(opponent == "Paper"):
            print("You won! :) ")
            scoreWin += 1

    elif (opt == '1'):
        print( "Wins: {} \nLosses: {}".format(scoreWin, scoreLose) )

    else:
        print("Invalid Option")
