from typing import List, Dict
from scoring import Scoring
from dice import YahtzeeDice
from display_Dice import display_dice

class Player:

    player_id = 0

    def __init__(self):
            Player.player_id += 1
            if Player.player_id ==1:
                self.id = Player.player_id
                print("---------------------------------------------------------------")
                print(f"Player {self.id}, Ai ")
                self.name = "Ai"
            else:
                self.id = Player.player_id
                print("---------------------------------------------------------------")
                print(f"Player {self.id}, enter your name: ")
                self.name = input()
    def get_name(self):
        return self.name
        

    def get_id(self):
        return self.id
class PlayerTurn():
    def __init__(self,initial_cal):
    # Initialize YahtzeeDice object
        yahtzee_set = YahtzeeDice()
        values = [None] * yahtzee_set.num_dice
        held_indices = []
        print("---------------------------------------------------------------")  
        print("Are you ready to roll the dice?")
        display_dice(values)
                # Roll the dice and display
        input("Press Enter to roll the dice")
        yahtzee_set = YahtzeeDice(initial_matrix=[None, None, None, None, None])
        values = yahtzee_set.roll_all()
        display_dice(values)
        for i in range(1,3):


            # Ask the player to determine which dice to keep
            keep_indices = input("Enter the numbers (1-5) of dice you want to keep (separated by spaces): ")
            
            constant_dice = keep_indices.split()
            # Create a new matrix values2 with None at all positions
            values2 = [None] * len(values)

            # Iterate through the input numbers and update values matrix
            for i, num in enumerate(constant_dice):
                num = int(num)
                if 1 <= num <= 5:
                    index = num - 1  # Adjust for 0-based indexing
                    if 0 <= index < len(values):
                        values2[index] = values[index]
            
            
            keep_indices = list(map(int, keep_indices.split()))
            held_indices = [i - 1 for i in keep_indices if 1 <= i <= 5]

            # Roll the remaining dice and display
            yahtzee_set = YahtzeeDice(initial_matrix=values2)
            values = yahtzee_set.roll_all()
            display_dice(values, held_indices)
        yahtzee_game = Scoring(values, initial_cal)

        self.total_score, self.updated_matrix = yahtzee_game.calculate_score()

    def get_total_score(self):
        return self.total_score

    def get_updated_matrix(self):
        return self.updated_matrix

if __name__ == "__main__":
    fd = PlayerTurn()
    print(f"Player {1}: {PlayerTurn.updated_matrix()}") 
