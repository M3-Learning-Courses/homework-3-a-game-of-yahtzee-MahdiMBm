import random
import time
from display_Dice import display_dice
from scoring import Scoring

# Dice Selection:
# 1. Adaptive Strategy: Adapts dice selection based on available and selected categories, prioritizing potential high-scoring categories.
# 2. Dynamic Approach: Considers game state and potential scoring opportunities, avoiding unnecessary risks leading to zero scores.
# 3. Specialized Logic: Implements specific logic for keeping dice in certain situations, like prioritizing dice for Three-of-a-Kind or Four-of-a-Kind.

# Category Selection:
# 1. Smart Prioritization: Prioritizes categories with the highest potential scores, considering current dice configuration and available categories.
# 2. Bonus Consideration: Utilizes bonus points for upper section categories when applicable, maximizing overall score.
# 3. Yahtzee Handling: Addresses Yahtzee scoring intricacies by intelligently choosing between Yahtzee and Chance when no matching combination is achieved.

# Overall Strategy:
# 1. Adaptive Decision-Making: Adapts strategy based on game state, available categories, and previously selected categories for dynamic gameplay.
# 2. Strategic Risk Management: Balances risk and reward, avoiding unnecessary risks leading to low scores in crucial categories.
# 3. Efficient Resource Utilization: Maximizes scoring potential by strategically selecting categories aligned with the current dice configuration.

class PlayerTurn_ai:
    def __init__(self, initial_cal):
        self.dice = [0] * 5
        self.kept_dice = []
        self.initial_cal = initial_cal
        self.total_score = 0
        self.best_category = ""
        self.score = 0
        self.selected_categories = []  # Keep track of previously selected categories

        # Simulate three rolls
        for roll_num in range(1, 4):
            self.roll_and_keep_dice()
            time.sleep(2)

        # Create YahtzeeAI instance, passing current dice, initial score matrix, and selected categories
        yahtzee_ai = YahtzeeAI(self.dice, self.initial_cal, self.selected_categories)
        self.total_score, self.initial_cal, self.best_category, self.score = yahtzee_ai.select_best_category()

    def roll_and_keep_dice(self):
        # Roll the dice and decide which dice to keep
        self.dice = [random.randint(1, 6) if i not in self.kept_dice else self.dice[i] for i in range(5)]
        print("                            AI Player is thinking")

        # Pass the list of selected categories to the dice selection function
        available_categories = [cat for cat in self.initial_cal if cat == ""]
        self.kept_dice.extend(select_dice_to_keep(self.dice, self.selected_categories, available_categories))

        display_dice(self.dice, self.kept_dice)

    def get_updated_matrix(self):
        return self.initial_cal

    def get_best_category(self):
        return self.best_category

    def get_score(self):
        return self.score

    def get_total_score(self):
        return self.total_score

    def get_initial_matrix(self):
        return self.initial_cal


def select_dice_to_keep(dice, selected_categories, available_categories):
    # AI's decision-making logic for selecting dice to keep
    # Prioritize keeping dice that match potential high-scoring categories

    # Example: Adjust the logic based on the selected and available categories
    if "Yahtzee" in available_categories:
        # If Yahtzee is available, keep all dice and choose Yahtzee if applicable
        return [0, 1, 2, 3, 4]

    for category in selected_categories:
        if category in ["Three-of-a-Kind", "Four-of-a-Kind"]:
            # If Three-of-a-Kind or Four-of-a-Kind is selected, prioritize keeping dice with the same value
            target_value = int(category.split("-")[0])  # Extract the target value (e.g., 3 for Three-of-a-Kind)
            return [i for i, value in enumerate(dice) if value == target_value]

    # Prioritize keeping dice that contribute to potential high-scoring categories
    potential_high_scoring_dice = get_potential_high_scoring_dice(dice, selected_categories)
    
    if potential_high_scoring_dice:
        return potential_high_scoring_dice

    # If no specific strategy is applicable, keep the highest count dice
    counts = [dice.count(i) for i in range(1, 7)]
    max_count = max(counts)
    kept_dice = [i for i, value in enumerate(dice) if dice.count(value) == max_count]

    return kept_dice


def get_potential_high_scoring_dice(dice, selected_categories):
    # Identify and return dice that contribute to potential high-scoring categories
    high_scoring_dice = []

    for category in selected_categories:
        if category in ["Small Straight", "Large Straight"]:
            # For Small Straight or Large Straight, keep dice that contribute to the sequence
            high_scoring_dice.extend(get_straight_dice(dice))
        elif category in ["Full House"]:
            # For Full House, keep dice that match the count required for a Full House
            high_scoring_dice.extend(get_full_house_dice(dice))
        # Add more conditions for other potential high-scoring categories

    return high_scoring_dice


def get_straight_dice(dice):
    # Helper function to get dice that contribute to a straight sequence
    unique_values = set(dice)

    # If there are four consecutive values, return the dice that break the sequence
    for value in unique_values:
        if value + 1 in unique_values and value + 2 in unique_values and value + 3 in unique_values:
            return [i for i, die in enumerate(dice) if die != value + 1 and die != value + 2 and die != value + 3]

    return []


def get_full_house_dice(dice):
    # Helper function to get dice that contribute to a Full House
    counts = [dice.count(i) for i in set(dice)]
    
    # If there is a pair and a three-of-a-kind, return the dice that are not part of the Full House
    if 2 in counts and 3 in counts:
        pair_value = [i for i, count in enumerate(counts) if count == 2][0]
        three_of_a_kind_value = [i for i, count in enumerate(counts) if count == 3][0]
        
        return [i for i, die in enumerate(dice) if die != pair_value and die != three_of_a_kind_value]

    return []


class YahtzeeAI:
    def __init__(self, dice_values, initial_cal, selected_categories):
        self.dice_values = dice_values
        self.initial_cal = initial_cal
        self.selected_categories = selected_categories  # Receive selected categories from PlayerTurnAI

    def evaluate_category(self, category):
        # Evaluate the potential score for a given category
        scoring = Scoring(self.dice_values, self.initial_cal)
        return scoring.yahtzee_score(category)

    def select_best_category(self):
        categories = [
            "Aces", "Twos", "Threes", "Fours", "Fives",
            "Sixes", "Three-of-a-Kind", "Four-of-a-Kind",
            "Full House", "Small Straight", "Large Straight",
            "Yahtzee", "Chance"
        ]

        available_categories = [cat for cat in categories if self.initial_cal[categories.index(cat)] == ""]
        bonus_available = sum(filter(lambda x: isinstance(x, (int, float)), self.initial_cal[:6])) >= 63

        best_category = available_categories[0]
        max_score = self.evaluate_category(best_category)

        # Iterate over available categories to find the one with the highest potential score
        for category in available_categories[1:]:
            score = self.evaluate_category(category)

            # Add bonus points if applicable (for the upper section categories)
            if bonus_available and categories.index(category) < 6:
                score += 35

            # Update the best category if a higher score is found
            if score > max_score:
                max_score = score
                best_category = category

        # Handle Yahtzee separately to avoid confusion with bonus points
        if best_category == "Yahtzee" and max_score == 0:
            best_category = "Chance"

        # Update the initial_cal matrix with the chosen category and its score
        index_of_best_category = categories.index(best_category)
        self.initial_cal[index_of_best_category] = max_score

        # Update the total score
        total_score = sum(filter(lambda x: isinstance(x, int), self.initial_cal))

        # print([total_score, self.initial_cal, best_category, max_score])
        print("--------------------------------------------------------------------------------------")  
        print(f"|  AI selected --> {best_category}: {max_score}      |     The total score for AI is:   {total_score}   |")

        # Keep track of the selected category for future dice selection
        if best_category not in self.selected_categories:
            self.selected_categories.append(best_category)

        return total_score, self.initial_cal, best_category, max_score


if __name__ == "__main__":
    initial_matrix = [""] * 14
    for i in range(0, 13):
        PlayerTurn_ai(initial_matrix)
