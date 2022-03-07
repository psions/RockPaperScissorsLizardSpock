from random import random


class AI_Choice:
    
    def AI_Choice():
        choice = str(random.randint(0,4))
        if choice == "0":
            print(" AI chose Rock")
        elif choice == "1":
            print(" AI chose Paper")
        elif choice == "2":
            print(" AI chose scissors")
        elif choice == "3":
            print(" AI chose Lizard")
        elif choice == "4":
            print("AI chose Spock, live long and prosper")
        return choice
