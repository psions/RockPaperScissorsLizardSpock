import random
from player import Player
from ai import AI
from human import Human




# (5 points): As a developer, I want to make at least 10 commits with descriptive messages.

# (15 points): As a developer, I want to find a way to properly incorporate inheritance into my game.

# (5 points): As a developer, I want to account for and handle bad user input, ensuring that any user input is validated and reobtained if necessary.

# (10 points): As a developer, I want to store all of the gesture options/choices in a list. I want to find a way to utilize the list of gestures within my code (display gesture options, assign player a gesture, etc).

# NOTE: Do not use a Gesture class until you have reached MVP for all user stories and been checked off by an instructor!

# (10 points): As a player, I want the correct player to win a given round based on the choices made by each player. See Framework document for game rules!

# (10 points): As a player, I want the game of RPSLS to be at minimum a “best of three” to decide a winner.

# (10 points): As a player, I want the option of a single player (human vs AI) or a multiplayer (human vs human) game
class Game_Board:
    def __init__(self):
        self.chosen_gesture = ""
        self.player_one = Human()
        self.player_two = None
    
    def run_game(self):
        self.display_greeting()
        self.rules_of_game()
        self.single_or_multiplayer()
        self.display_gesture_options()
    
    def display_greeting(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock")
        print("")

    def rules_of_game(self):
        print("Rock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock")
        print("")

    def single_or_multiplayer(self):
        choice = int(input("Do you want to play solo (1) or multiplayer (2): "))
    
        if choice == 1:
            print("You are playing Solo")
            self.solo_game()
            self.player_two = AI_Choice()
        elif choice == 2:
            print("You are playing Multiplayer")
            self.multiplayer()
            self.player_two = Human()

    def display_gesture_options(self): 
        count = 0
        gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        for item in gesture_list:
            print(f"Enter {count} to use {item}")
            count += 1    
        


    def compare_gestures(self):
        pass

    def determine_round_winner(self):
        pass

    def check_game_score(self):
        pass

    def solo_game(self):
        pass

    def multiplayer(self):
        pass

    def play_again(self):
        pass