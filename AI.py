import random
from unicodedata import name
from player import Player
from time import sleep


class AI(Player):
        
    def __init__(self):
        super().__init__(name)

    def choose_gesture(self):
        self.chosen_gesture = random.choice(self.gestures)
        print(f"AI Chose{self.chosen_gesture}")
        
        