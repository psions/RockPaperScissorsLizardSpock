class Player:
    
    def PlayerChoice():
        choice = int(input(" What do you choose?"))
        if choice == 0:
            print(" You chose Rock")
        elif choice == 1:
            print(" You chose Paper")
        elif choice == 2:
            print(" You chose scissors")
        elif choice == 3:
            print(" You chose Lizard")
        elif choice == 4:
            print("You chose Spock, live long and prosper")
        elif choice > 4:
            print(" Invalid Entry, Try Again!")
        elif choice < 0:
            print(" Invalid Entry, Try Again!")
        return choice
