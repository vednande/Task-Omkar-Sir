from abc import ABC, abstractmethod

class Sports:

    score_A = 0
    score_B = 0

    def __init__(self) -> None:
        pass
    
    def toss(self):
        print("Toss called 1")

    def increment(self):
        pass

    def tie_breaker(self):
        pass

    def is_winner(self):
        pass

class Badminton(Sports):

    def increment(self):
        print("Increment called of Bad")

    def is_winner(self):
        pass

class Tennis(Sports):

    def increment(self):
        print("Increment called of Tennis")

    def is_winner(self):
        pass

class Table_Tennis(Sports):
    
    def increment(self):
        pass

    def is_winner(self):
        pass

def main_func():

    bad = Badminton()
    ten = Tennis()
    tt = Table_Tennis()

    while True:
        var = input("Start Game? ")

        if var == "yes" or var == "1":

            print("Select Game 👇")
            
            game = input("1. Badminton 2. Tennis 3. Table Tennis: ")

            play_game = None

            if game == "1":
                
                play_game = bad

            elif game == "2":

                play_game = ten

            elif game=="3":

                play_game = tt

            elif game == "4":
                break

            else:
                print("Invalid Choice")

            # calling toss 
            play_game.toss()

            while True:
                # making user decide
                round = input("A or B: ")

                if round == "A":
                    play_game.increment()

        else:
            break 


main_func()