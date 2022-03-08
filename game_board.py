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
        self.player_one = Human("player 1")
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
            print("You chose single player")
            self.player_two = AI("player 2")
            self.solo_game()
            
        elif choice == 2:
            print("You chose multiplayer")
            self.player_two = Human("player 2")
            self.multiplayer()
            
    def compare_choices(self):
    
        if Human.chosen_gesture == AI.chosen_gesture:
            print("tie")


        elif Human.chosen_gesture == "Rock":
            if AI.chosen_gesture == "Paper":
                print("Player 2 is the winner")
                AI.score += 1
            elif AI.chosen_gesture == "scissors":
                print("Player 1 is the winner")
                Human.score +=1
            elif AI.chosen_gesture == "Lizard":
                print("Player 1 is the winner")
                Human.score +=1
            elif AI.chosen_gesture == "Spock":
                print("Player 2 is the winner")
                AI.score += 1


        elif Human.chosen_gesture == "Paper":
            if AI.chosen_gesture == "scissors":
                print("Player 2 is the winner")
                AI.score += 1
            elif AI.chosen_gesture == "Rock":
                print("Player 1 is the winner")
                Human.score +=1
            elif AI.chosen_gesture == "Lizard":
                print("Player 2 is the winner")
                AI.score += 1
            elif AI.chosen_gesture == "Spock":
                print("Player 1 is the winner")
                Human.score +=1

        elif Human.chosen_gesture == "Scissors":
            if AI.chosen_gesture == "Paper":
                print("Player 1 is the winner")
                Human.score +=1
            elif AI.chosen_gesture == "Rock":
                print("Player 2 is the winner")
                AI.score += 1
            elif AI.chosen_gesture == "Lizard":
                print("Player 1 is the winner")
                Human.score +=1
            elif AI.chosen_gesture == "Spock":
                print("Player 2 is the winner")
                AI.score += 1

        elif Human.chosen_gesture == "Lizard":
            if AI.chosen_gesture =="Rock":
                print("Player 2 is the winner")
                AI.score += 1
            elif AI.chosen_gesture == "Paper":
                print("Player 1 is the winner")
                Human.score +=1
            elif AI.chosen_gesture =="Scissors":
                print("Player 2 is the winner")
                AI.score += 1
            elif AI.chosen_gesture == "Spock":
                print("Player 1 is the winner")
                Human.score +=1

        elif Human.chosen_gesture == "Spock":
            if AI.chosen_gesture == "Rock":
                print("Player 1 is the winner")
                Human.score +=1
            elif AI.chosen_gesture == "Paper":
                print("Player 2 is the winner")
                AI.score += 1
            elif AI.chosen_gesture == "Scissors":
                print("Player 1 is the winner")
                Human.score +=1
            elif AI.chosen_gesture == "Lizard":
                print("Player 2 is the winner")
                AI.score += 1

    def determine_round_winner(self):
        pass

    def check_game_score(self):
        pass
        

    def solo_game(self):
        Human.choose_gesture(self)
        AI.choose_gesture(self)
        compare_choices()
        pass
    def multiplayer(self):
        pass

    def play_again(self):
        pass