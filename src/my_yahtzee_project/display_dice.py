from typing import List

def display_dice(values: List[int], held_indices: List[int] = []):
    """
    Display the ASCII art representation of dice values, with optional color coding for held dice.

    Args:
        values (List[int]): A list of integers representing the current face-up values of the dice.
        held_indices (List[int], optional): A list of integers representing the indices of held dice (default is an empty list).

    Returns:
        None
    """
    # Define ASCII art for dice faces
    dice_faces = {
        None: [
            "-----",
            "|   |",
            "| ? |",
            "|   |",
            "-----"
        ],
        1: [
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "-----"
        ],
        2: [
            "-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----"
        ],
        3: [
            "-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----"
        ],
        4: [
            "-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----"
        ],
        5: [
            "-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----"
        ],
        6: [
            "-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----"
        ]
    }

    # ANSI color codes for text color
    ANSI_COLOR = {
        'default': "\033[0m",
        'green': "\033[92m"
    }

    # Initialize the display strings for each row
    display_str = [""] * 5

    for i, value in enumerate(values):
        die = dice_faces.get(value, [])
        if not die:
            continue

        # Check if the die is held
        is_held = i in held_indices

        # Choose the color for the die
        color = ANSI_COLOR['green'] if is_held else ANSI_COLOR['default']

        # Iterate over each row of the die face and add to the corresponding row in the display string
        for j, row in enumerate(die):
            display_str[j] += color + row + ANSI_COLOR['default'] + "  "

    # Print the ASCII art vertically
    for row in display_str:
        print(row)

# Example usage:
if __name__ == "__main__":
    values = [4, 2, 6, 4, 3]
    held_indices = [1,2]
    display_dice(values, held_indices)
