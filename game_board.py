import random
import player
import AI


# (5 points): As a developer, I want to make at least 10 commits with descriptive messages.

# (15 points): As a developer, I want to find a way to properly incorporate inheritance into my game.

# (5 points): As a developer, I want to account for and handle bad user input, ensuring that any user input is validated and reobtained if necessary.

# (10 points): As a developer, I want to store all of the gesture options/choices in a list. I want to find a way to utilize the list of gestures within my code (display gesture options, assign player a gesture, etc).

# NOTE: Do not use a Gesture class until you have reached MVP for all user stories and been checked off by an instructor!

# (10 points): As a player, I want the correct player to win a given round based on the choices made by each player. See Framework document for game rules!

# (10 points): As a player, I want the game of RPSLS to be at minimum a “best of three” to decide a winner.

# (10 points): As a player, I want the option of a single player (human vs AI) or a multiplayer (human vs human) game

def rules_of_game():
    rules = print( " Rock crushes Scissors, /n Scissors cuts Paper, /n Paper covers Rock, /n Rock crushes Lizard, /n Lizard poisons Spock,/n Spock smashes Scissors, /n Scissors decapitates Lizard, /n Lizard eats Paper, /n Paper disproves Spock, /n Spock vaporizes Rock ")


    print(rules)
## Greeting under this

def display_greeting():
    print("Welcome to Rock, Paper, Scissors, Lizard, Spock")


def single_or_multiplayer():
    choice = int(input("Do you want to play solo (1) or multiplayer (2): "))
    
    if choice == 1:
        print("You are playing Solo")
    elif choice == 2:
        print("You are playing Multiplayer")



def display_gesture_options(): 
    pass 

def compare_gestures():
    pass

def determine_round_winner():
    pass

def check_game_score():
    pass

def play_again():
    pass
