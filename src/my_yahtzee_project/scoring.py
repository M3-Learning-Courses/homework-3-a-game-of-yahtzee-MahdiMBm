import tkinter as tk
from tkinter import ttk
from itertools import combinations
from collections import Counter

class Scoring:
    def __init__(self, dice_values, initial_matrix):
        """
        Initializes a scoring object for a Yahtzee game.

        Parameters:
        - dice_values (list): List of five integers representing dice values.
        - initial_matrix (list): Represents the matrix of categories and bonuses.
        Returns:
        - Scoring object: An instance of the Scoring class.
        """
        self.dice_values = dice_values
        self.initial_matrix = initial_matrix

    def yahtzee_score(self, category):
        """
        Calculates the score for a given category.
        Parameters:
        - category (str): A string representing the category for which to calculate the score.
        Returns:
        - int: The score for the given category.
        """
        if category == "Aces":
            return self.dice_values.count(1) * 1
        elif category == "Twos":
            return self.dice_values.count(2) * 2
        elif category == "Threes":
            return self.dice_values.count(3) * 3
        elif category == "Fours":
            return self.dice_values.count(4) * 4
        elif category == "Fives":
            return self.dice_values.count(5) * 5
        elif category == "Sixes":
            return self.dice_values.count(6) * 6
        elif category == "Three-of-a-Kind":
            for num in set(self.dice_values):
                if self.dice_values.count(num) >= 3:
                    return sum(self.dice_values)
            return 0
        elif category == "Four-of-a-Kind":
            for num in set(self.dice_values):
                if self.dice_values.count(num) >= 4:
                    return sum(self.dice_values)
            return 0
        elif category == "Full House":
            counts = [self.dice_values.count(num) for num in set(self.dice_values)]
            if 2 in counts and 3 in counts:
                return 25
            return 0
        elif category == "Small Straight":
            for combo in combinations(set(self.dice_values), 4):
                if max(combo) - min(combo) == 3:
                    return 30
            return 0
        elif category == "Large Straight":
            if len(set(self.dice_values)) == 5 and max(self.dice_values) - min(self.dice_values) == 4:
                return 40
            return 0
        elif category == "Yahtzee":
            for num in set(self.dice_values):
                if self.dice_values.count(num) == 5:
                    return 50
            return 0
        elif category == "Chance":
            return sum(self.dice_values)
        else:
            return 0

    def calculate_score(self):
        """
        Initiates a GUI to calculate and display the scores for each category.

        Returns:
        - tuple: A tuple containing the total score and the updated matrix of categories and bonuses.
        """
        # GUI setup

    
        root = tk.Tk()
        root.title("Yahtzee Scorer")

        # Display dice numbers in five columns at the top
        for i, value in enumerate(self.dice_values):
            ttk.Label(root, text=value).grid(row=0, column=i, padx=5, pady=5)

        # Display scores for each category
        score_frame = ttk.Frame(root)
        score_frame.grid(row=1, column=0, columnspan=5, pady=10)

        categories = [
            "Aces", "Twos", "Threes", "Fours", "Fives",
            "Sixes", "Three-of-a-Kind", "Four-of-a-Kind",
            "Full House", "Small Straight", "Large Straight",
            "Yahtzee", "Chance"
        ]

        for category in categories:
            ttk.Label(score_frame, text=category).grid(row=categories.index(category), column=0, padx=5, pady=5)
            if self.initial_matrix[categories.index(category)] == "":
                score = self.yahtzee_score(category)
                ttk.Label(score_frame, text=score).grid(row=categories.index(category), column=1, padx=5, pady=5)

        # Category selection
        category_combobox = ttk.Combobox(root, values=[cat for cat in categories if self.initial_matrix[categories.index(cat)] == ""])
        category_combobox.grid(row=2, column=0, columnspan=5, pady=10)

        # Calculate button
        def update_matrix_and_close():
            selected_category = category_combobox.get()
            index = categories.index(selected_category)

            if self.initial_matrix[index] == "":
                self.initial_matrix[index] = self.yahtzee_score(selected_category)

            root.destroy()

        calculate_button = tk.Button(root, text="Calculate Score", command=update_matrix_and_close)
        calculate_button.grid(row=3, column=0, columnspan=5, pady=10)

        # Display total score at the lower section
        total_score_label = ttk.Label(root, text="")
        total_score_label.grid(row=5, column=0, columnspan=5, pady=5)

        # Update total score label
        def update_total_score_label():
            total_score_label.config(text=f"Total Score: {sum(filter(lambda x: isinstance(x, int), self.initial_matrix))}")

        update_total_score_label()

        if sum(filter(lambda x: isinstance(x, (int, float)), self.initial_matrix[:6])) >= 63:
            ttk.Label(root, text="Bonus +35").grid(row=4, column=0, columnspan=5, pady=10)

        root.mainloop()

        if sum(filter(lambda x: isinstance(x, (int, float)), self.initial_matrix[:6])) >= 63:
            self.initial_matrix[13] = 35

        total_score = sum(filter(lambda x: isinstance(x, int), self.initial_matrix))
        return total_score, self.initial_matrix

if __name__ == "__main__":
    # Example usage:
    initial_matrix = [""] * 14  # Represents the matrix of categories and bonuses
    dice_values = [5, 5, 5, 5, 5]

    # First call to the function
    yahtzee_game = Scoring(dice_values, initial_matrix)
    total_score, updated_matrix = yahtzee_game.calculate_score()
    print(f"Total Score: {total_score}")
    print(f"Updated Matrix: {updated_matrix}")

    dice_values = [6, 6, 6, 6, 6]

    # Second call to the function
    yahtzee_game = Scoring(dice_values, initial_matrix)
    total_score, updated_matrix = yahtzee_game.calculate_score()
    print(f"Total Score: {total_score}")
    print(f"Updated Matrix: {updated_matrix}")

    dice_values = [4, 4, 4, 4, 4]

    # Third call to the function
    yahtzee_game = Scoring(dice_values, initial_matrix)
    total_score, updated_matrix = yahtzee_game.calculate_score()
    print(f"Total Score: {total_score}")
    print(f"Updated Matrix: {updated_matrix}")

    dice_values = [3, 3, 3, 3, 3]

    # Fourth call to the function
    yahtzee_game = Scoring(dice_values, initial_matrix)
    total_score, updated_matrix = yahtzee_game.calculate_score()
    print(f"Total Score: {total_score}")
    print(f"Updated Matrix: {updated_matrix}")
