from player import Player

class Human(Player):

    def __init__(self, name):
        super().__init__(name)
    
    def choose_gesture(self):
        count = 0
        for item in self.gestures:
            
            print(f"Enter {count} to use {item}")
            count += 1
        player_choice = input("Make your choice: ")
        if player_choice == "0":
            self.chosen_gesture = self.gestures[0]
            print("You have chosen Rock")
        if player_choice == "1":
            self.chosen_gesture = self.gestures[1]
            print("You have chosen Paper")
        if player_choice == "2":
            self.chosen_gesture = self.gestures[2]
            print("You have chosen Scissors")
        if player_choice == "3":
            self.chosen_gesture = self.gestures[3]
            print("You have chosen Lizard")
        if player_choice == "4":
            self.chosen_gesture = self.gestures[4]
            print("You have chosen Spock")
            
