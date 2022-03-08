from AI import AI

# Rock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\n
# Spock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock")



if player == AI:
    print("tie")


elif player == "Rock":
    if AI == "paper":
        print("You lose" {AI} "covers" {player})
    elif AI == "scissors":
        print("You Win", {player} "crushes" {AI})
    elif AI == "Lizard":
        print("You win", {player}"crushes" {AI})
    elif AI == "Spock":
        print("You lose", {AI}, "Vaporizes" {player})


elif player == "Paper":
    if AI == "scissors":
        print("You lose", {AI} "cuts" {player})
    elif AI == "Rock":
        print("You win", {player} "covers" {AI})
    elif AI == "Lizard":
        print("You Lose" {AI} "eats" {player}) 
    elif AI == "Spock":
        print("You win", {player} "disproves" {AI})

elif player == "Scissors":
    if AI == "Paper":
        print("You Win", {player} "cuts {AI}")
    elif AI == "Rock":
        print("You Lose" {AI} "crushes" {player})
    elif AI == "Lizard":
        print("You Win" {player} "Decapitates" {AI})
    elif AI == "Spock":
        print("You Lose" {AI} "Smashes" {player})

elif player == "Lizard":
    if AI =="Rock":
        print("You Lose", {AI} "Crushes" {player})
    elif AI == "Paper":
        print("You Win", {Player} "Eats" {AI})
    elif AI =="Scissors":
        print("You lose", {AI} "Decapitates" {player})
    elif AI == "Spock":
        print("You Win", {player} "poisons" {AI})

elif player == "Spock":
    if AI == "Rock":
        print("You win", {player} "Vaporizes" {AI})
    elif AI == "Paper":
        print(" You Lose" {AI} "disproves" {player})
    elif AI == "Scissors":
        print("You Win", {player} "smashes" {AI})
    elif AI == "Lizard":
        print("You lose" {AI} "Poisons" {player})


