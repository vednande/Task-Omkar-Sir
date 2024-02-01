# this is done by ved nande
# gandu ved hai 
class Sports:
    def __init__(self,player1,player2):
        
        self.player1=player1
        self.player2=player2

        self.score_A = 0
        self.score_B = 0

        self.set_won_A = 0
        self.set_won_B = 0

        self.game_won_A = 0
        self.game_won_B = 0

        self.current_game = 0

        self.current_set = 1

        self.scoreList=[]
        
    def toss(self,input):
        print(f"\nToss won by team {input}, {input} will start Serving ")

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
        print("Score Board ....  ")
        print("(SET No : [score of A, Score of B])\n")
        print(self.scoreList)
    def increment(self,round):
        if round == "A" or "a" :
            self.score_A +=1
        elif round == "B" or "b":
            self.score_B +=1
        else :
            return (print("Invalid Input"))

        print(f"A = {self.score_A} and B = {self.score_B}")
      
    def is_setwinner(self):
        if (((self.score_A >= 21 and self.score_A<30) and (self.score_A -self.score_B >=2))) or (self.score_A == 30):
            self.set_won_A +=1
            self.scoreList.append({self.current_set:[self.score_A,self.score_B]})
            self.current_set +=1
            self.score_A = 0
            self.score_B =0
            if self.set_won_A <2:
                return print(f" Set Completed !! Next Set Starting ...")
        elif (((self.score_B >= 21 and self.score_B<30) and (self.score_B -self.score_A >=2))) or (self.score_B == 30):
            self.set_won_B +=1
            self.scoreList.append({self.current_set:[self.score_A,self.score_B]})
            self.current_set +=1
            self.score_A = 0
            self.score_B =0
            if self.set_won_B <2:
                return print(f" Set Completed !! Next Set Starting ...")
        else:
            pass
    
    def is_overallwinner(self):
        if self.set_won_A == 2:
            return self.player1
        elif self.set_won_B == 2:
            return self.player2
        else :
            pass
        


'''
    VED NANDE CODE GOES HERE 👇
'''
class Tennis(Sports):
    def view_score(self):
        # print("Score Board ....  ")
        # print("(SET No : [Game A, Game B, Set A, Set B])\n")
        # print(self.scoreList)
        pass

    def increment(self, point_winner):
        if point_winner.lower() == "a":
            self.score_A += 1

        elif point_winner.lower() == "b":
            self.score_B += 1

        else:
            return print("Invalid Input")

        print(f"Game Score: A = {self.score_A}, B = {self.score_B}")


    def tie_breaker(self):

        print("TIE BREAKER")

        while self.score_A <= 5 or self.score_B <= 5:

            round = input("A or B: ")

            count = []

            if round == "A":
                    self.score_A += 1
                    
                    count.append(round)

                    if self.score_A == 5 and self.score_B == 3:
                        self.game_won_A += 1
                        print(f"\nTIE BREAKER DONE ==== GAME POINT || A = {self.game_won_A} || B = {self.game_won_B}\n")
                        self.score_A = 0
                        self.score_B = 0
                        return
                        
            else:
                self.score_B += 1
                if self.score_B == 5 and self.score_A == 3:
                        self.game_won_B += 1

                        count.append(round)

                        print(f"\nTIE BREAKER DONE ==== GAME POINT || A = {self.game_won_A} || B = {self.game_won_B}\n")
                        self.score_A = 0
                        self.score_B = 0
                        return
                        
    def game_tie(self):
        round = input("A or B: ")

        if round == "A":
            self.game_won_A += 1

            if self.game_won_A == 4 and self.game_won_B == 3:
                self.set_won_A += 1
                print(f"\nTIE BREAKER DONE ==== GAME POINT || A = {self.game_won_A} || B = {self.game_won_B}\n")
                self.score_A = 0
                self.score_B = 0
                return
                        
            else:
                self.game_won_B += 1
                if self.game_won_B == 4 and self.score_A == 3:
                    self.set_won_B += 1
                    print(f"\nTIE BREAKER DONE ==== GAME POINT || A = {self.game_won_A} || B = {self.game_won_B}\n")
                    self.score_A = 0
                    self.score_B = 0
                    return



    def is_setwinner(self):

        if (self.score_A == 3 and self.score_B == 3):
            self.tie_breaker()
            


        if ((self.score_A >= 4 and self.score_A - self.score_B >= 2) or (self.score_A == 4)) or ((self.score_B >= 4 and self.score_B - self.score_A >= 2) or (self.score_B == 4)):

            if self.score_A > self.score_B:
                # self.set_won_A += 1
                self.game_won_A += 1
                print(f"\n is_setwinner GAME POINT || A = {self.game_won_A} || B = {self.game_won_B}\n")
                
            elif self.score_B > self.score_A:
                # self.set_won_B += 1
                self.game_won_B += 1
                print(f"\n is_setwinner GAME POINT || A = {self.game_won_A} || B = {self.game_won_B}\n")

            # self.scoreList.append([self.game_won_A, self.game_won_B, self.set_won_A, self.set_won_B])
            # self.game_won_A = 0
            # self.game_won_B = 0
            self.score_A = 0
            self.score_B = 0

            if ((self.game_won_A + self.game_won_B == 6) or (self.game_won_A > self.game_won_B and self.game_won_A == 4) ):

                if self.game_won_A ==3 and self.game_won_B == 3:
                    self.game_tie()

                self.set_won_A +=1
                print(f"SET || A = {self.set_won_A} || B = {self.set_won_B}\n")
                self.game_won_A = 0
                self.game_won_B = 0
            
            elif (self.game_won_A + self.game_won_B == 6 and self.game_won_A < self.game_won_B):
                self.set_won_B +=1
                print(f"SET || A = {self.set_won_A} || B = {self.set_won_B}\n")
                self.game_won_A = 0
                self.game_won_B = 0

    def is_overallwinner(self):
        if self.set_won_A == 2:
            return self.player1
        elif self.set_won_B == 2:
            return self.player2
        else:
            pass


class Table_Tennis(Sports):



    def view_score(self):
        print("Score Board  ")
        print(f"{self.player1}={self.score_A}")
        print(f"{self.player2}={self.score_B}")
    
    def increment(self, round):
        round = round.upper()  # Convert input to uppercase for consistent comparison
        if round == "A":
            self.score_A += 1
        elif round == "B":
            self.score_B += 1
        else:
            return print("Invalid Input")

        print(f"A = {self.score_A} and B = {self.score_B}")

    def is_setwinner(self):
        '''Determines the winner of a set in table tennis.'''

        if (self._A >= 11 and (self._A - self._B >= 2)):
            self.set_A += 1
            self._A = 0
            self._B = 0
            if self.set_A < 4:
                return print(f"{self.current_set} won by {self.player1}.")
        else:
            self.set_B += 1
            self._A = 0
            self._B = 0
            if self.set_B < 4:
                return print(f"{self.current_set} won by {self.player2}.")
        if (self.score_A >= 11 and (self.score_A - self.score_B >= 2)):
            self.set_won_A += 1
            self.score_A = 0
            self.score_B = 0
            if self.set_won_A < 4:
                return print(
                    f"Game {self.current_set} won by {self.player1}. Game {self.current_set + 1} is now starting."
                )

        elif self.score_B >= 11 and (self.score_B - self.score_A >= 2):
            self.set_won_B += 1
            self.score_A = 0
            self.score_B = 0
            if self.set_won_B < 4:
                return print(
                    f"Game {self.current_set} won by {self.player2}. Game {self.current_set + 1} is now starting."
                )

        else:
            pass

    def is_overallwinner(self):
        if self.set_won_A == 2:
            return self.player1
        elif self.set_won_B == 2:
            return self.player2
        else :
            pass

def main_func():

    bad = Badminton("A","B")
    ten = Tennis("A","B")
    tt = Table_Tennis("A","B")

    while True: 
        var = input("Start Game? (yes/1 or no/0) ")

        if var == "yes" or var == "1":

            print("\nSelect Game 👇")
            
            print("\n1. Badminton\n2. Tennis\n3. Table Tennis:\n4. Exit\n")
            game = input("Select 1/2/3/4: ")

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
            toss=input("\nWho won the toss(A/B): ")
            play_game.toss(toss)

            while True:
                # making user decide
                round = input("A or B: ")

                play_game.increment(round)
                play_game.is_setwinner()
                x=play_game.is_overallwinner()

                if x:
                    print("---------")
                    print(f"TEAM {x} won the game .")
                    print("---------------")
                    play_game.view_score()
                    break


        else:
            break 


main_func()