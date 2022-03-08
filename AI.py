from random import random
from player import Player
from time import sleep


class AI(Player):
        
<<<<<<< HEAD
    def __init__(self, name):
=======
    def __init__(self):
>>>>>>> fccc0f77be3fe6c1c8d6e11946d48ce092478546
        super().__init__()
        self.gestures = None

    def choose_gesture(self):
        gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.gestures = random.choice(gestures)
        return super().choose_gesture()
        