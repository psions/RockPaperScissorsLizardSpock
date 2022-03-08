from random import random
from player import Player
from time import sleep


class AI(Player):
        
    def __init__(self, name):
        super().__ini__()
        self.gestures = None

    def choose_gesture(self):
        gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self. gestures = random.choice(gestures)
        return super().choose_gesture()
        