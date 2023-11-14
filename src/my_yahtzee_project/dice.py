import random
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Dice:
    """Represents a single dice with a specified number of sides.
    
    Attributes:
        sides (int): The number of sides on the dice.
        current_value (int): The current value obtained after rolling the dice.
    """
    sides: int = 6
    current_value: int = field(init=False, default=None)

    def roll(self):
        """Rolls the dice and updates the current value.
        
        Returns:
            int: The current value obtained after rolling the dice.
        """
        self.current_value = random.randint(1, self.sides)
        return self.current_value

@dataclass
class YahtzeeDice(Dice):
    """Represents a set of dice for a Yahtzee game, inheriting properties from the Dice class.

    Attributes:
        num_dice (int): The number of dice in the Yahtzee set.
        dice_set (List[Dice]): The set of dice.
        initial_matrix (for example[3, 6, None, None, 1]): Initial values for the dice set.
        It determines which dice should be rolled and which of them are determined.
    """
    num_dice: int = 5
    dice_set: List[Dice] = field(init=False)
    initial_matrix: Optional[List[Optional[int]]] = None

    def __post_init__(self):
        """Initializes the rolling dice after checking the initial matrix.
        Adjusts the number of dice and creates the dice set based on the matrix if provided.
        """
        if self.initial_matrix is not None:
            self.num_dice = len(self.initial_matrix)
        self.dice_set = [Dice(sides=self.sides) for _ in range(self.num_dice)]

    def roll_all(self):
        """Rolls all dice in the set.
        If initial values are provided in the matrix, uses them; otherwise, rolls the dice.     
        Returns:
            List[int]: The current values obtained after rolling the dice set.
        """
        for i, die in enumerate(self.dice_set):
            if self.initial_matrix is not None and self.initial_matrix[i] is not None:
                die.current_value = self.initial_matrix[i]
            else:
                die.roll()
        return [die.current_value for die in self.dice_set]

    def get_values(self):
        return [die.current_value for die in self.dice_set]

# Example usage:
if __name__ == "__main__":
    # Pass an initial matrix with known values and None for unknown values
    yahtzee_set = YahtzeeDice(initial_matrix=[3, 6, None, None, 1])

    yahtzee_set.roll_all()
    print("Rolled values:", yahtzee_set.get_values())
