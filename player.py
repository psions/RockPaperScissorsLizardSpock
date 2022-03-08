class Player:
    
    
    def __init__(self):
        # self.name = name
        self.score = 0
        self.chosen_gesture = None


    def choose_gesture(self):
        self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        count = 0
        for item in self.gestures:
            print(f"Enter {count} to use {item}")
        player_choice = input("Make your choice: ")
        if player_choice == "0":
            self.chosen_gesture = self.gestures[0]
            print(f"{self.name} has chosen Rock")
        if player_choice == "1":
            self.chosen_gesture = self.gestures[1]
            print(f"{self.name} has chosen Paper")
        if player_choice == "2":
            self.chosen_gesture = self.gestures[2]
            print(f"{self.name} has chosen Scissors")
        if player_choice == "3":
            self.chosen_gesture = self.gestures[3]
            print(f"{self.name} has chosen Lizard")
        if player_choice == "4":
            self.chosen_gesture = self.gestures[4]
            print(f"{self.name} has chosen Spock")
