# this is done by ved nande
# gandu ved
class Sports:
    def __init__(self,player1,player2):
        
        self.player1=player1
        self.player2=player2
        self.score_A=0
        self.score_B=0
        self.set_won_A =0
        self.set_won_B =0
        self.current_set=1

        self.scoreList=[]
        
    def toss(self,input):
        print(f"Toss won by team {input},{input} will start Serving ")

    def increment(self):
        pass

    def tie_breaker(self):
        pass

    def is_setwinner(self):
        pass

    def is_overallwinner(self):
        pass

    def view_score(self):
        pass

class Badminton(Sports):
    def view_score(self):
        print("Score Board  ")
        print(f"{self.player1}={self.score_A}")
        print(f"{self.player2}={self.score_B}")
        

    def increment(self,round):
        if round == "A":
            self.score_A +=1
        elif round == "B":
            self.score_B +=1
        else :
            return (print("Invalid Input"))
      
    def is_setwinner(self):
        if (self.score_A >= 21 and (self.score_A -self.score_B >=2)) :
            self.set_won_A +=1
            # self.scoreList.append({set})
            self.score_A = 0
            self.score_B =0
            if self.set_won_A <2:
                return print(f"{self.current_set} has been won by {self.player1} and {self.current_set + 1} is starting ")
        
        elif self.score_B >= 21 and (self.score_B -self.score_A >=2):
            self.set_won_B +=1
            self.score_A = 0
            self.score_B =0
            if self.set_won_B <2:
                return print(f"Set {self.current_set} has been won by {self.player2} and Set {self.current_set + 1} is starting ")

        else:
            pass
    
    def is_overallwinner(self):
        if self.set_won_A == 2:
            return self.player1
        elif self.set_won_B == 2:
            return self.player2
        else :
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

    bad = Badminton("A","B")
    ten = Tennis("A","B")
    tt = Table_Tennis("A","B")

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
            toss=input("Who won the toss(A/B)")
            play_game.toss(toss)

            while True:
                # making user decide
                round = input("A or B: ")
                play_game.increment(round)
                play_game.is_setwinner()
                x=play_game.is_overallwinner()
                if x:
                    print(f"{x} won the game .")
                    break
            break

        else:
            break 


main_func()