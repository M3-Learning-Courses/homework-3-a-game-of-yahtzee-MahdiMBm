.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/my_yahtzee_project.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/my_yahtzee_project
    .. image:: https://readthedocs.org/projects/my_yahtzee_project/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://my_yahtzee_project.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/my_yahtzee_project/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/my_yahtzee_project
    .. image:: https://img.shields.io/pypi/v/my_yahtzee_project.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/my_yahtzee_project/
    .. image:: https://img.shields.io/conda/vn/conda-forge/my_yahtzee_project.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/my_yahtzee_project
    .. image:: https://pepy.tech/badge/my_yahtzee_project/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/my_yahtzee_project
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/my_yahtzee_project

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

|

==================
my_yahtzee_project
==================
Yahtzee Python Package
Objective
This Python package implements the logic for simulating dice rolls in a Yahtzee game. The project leverages Python’s object-oriented programming features and advanced data structures to accomplish this.

Rules of the Game of Yahtzee
Yahtzee is a dice game that combines elements of chance and strategy. Below are the detailed rules for playing Yahtzee:

Components
5 six-sided dice
A score sheet for each player to record scores
A cup for shaking dice (optional)
Objective
The objective of the game is to accumulate the highest score by rolling the five dice to make certain combinations, as outlined on the score sheet.

Number of Players
The game can be played by one or more players. Here, implementing the multi-player version of the game is performed.

Turn Sequence
Roll Dice: At the beginning of each turn, the player rolls all five dice.
Keep or Re-roll: After the initial roll, the player can choose to keep some or all dice and re-roll the remaining ones. This can be done up to two more times (for a total of three rolls per turn).
Scoring: After the final roll, the player must choose a category on their score sheet to fill in with the score from that turn. Each category can only be used once.
Scoring Categories
Upper Section
Aces: Sum of all aces rolled
Twos: Sum of all twos rolled
Threes: Sum of all threes rolled
Fours: Sum of all fours rolled
Fives: Sum of all fives rolled
Sixes: Sum of all sixes rolled
If a player scores at least 63 points in the upper section, they receive a bonus of 35 points.
Lower Section
Three-of-a-Kind: At least three dice showing the same face; scores the sum of those three dice.
Four-of-a-Kind: At least four dice showing the same face; scores the sum of those four dice.
Full House: A three-of-a-kind and a pair; scores a flat 25 points.
Small Straight: Four consecutive dice; scores a flat 30 points.
Large Straight: Five consecutive dice; scores a flat 40 points.
Yahtzee: All five dice showing the same face; scores a flat 50 points. Additional Yahtzees score a bonus.
Chance: Any combination; scores the sum of all five dice.


Installation
To install the required dependencies for this project, follow these steps:

Ensure Python and pip are installed:

If you don't have Python installed, download it from python.org.
Make sure to check the option that says "Add Python to PATH" during installation.
Download the Project:

Download or clone this project to your local machine.
Navigate to the Project Directory:

Open a command prompt and use the cd command to navigate to the root directory of the project.
Run the Installation Script:

Double-click on the install_dependencies.bat file in the project directory.
Alternatively, open a command prompt in the project directory and run the command: install_dependencies.bat
Verify Installation:

Check the command prompt for any error messages during the installation process.
Optionally, run pip list to ensure that the required packages are installed.



Usage
Run the "play_yahtzee" then you will be asked to enter the number of the users who want to play.
Each user will be asked to enter their name.
Five undetermined dice will be shown, and users will be asked to press enter for rolling dice.
The results of the rolling dice will be shown graphically, and the user can keep dice by entering their numbers (Enter the numbers (1-5) of dice you want to keep (separated by spaces)).
The previous step will be repeated.
A graphical window (named Yahtzee scorer) will be automatically opened. This window lets the user see possible scores in each selectable category and then select one of them. The score of the player is also presented until now.
The name of the second player will be shown, and they should do the same process one by one.
After finishing the steps for all players, the results will be shown, and a message for the winner will be seen.
The user will be asked whether they want to play again or not.


Troubleshooting and FAQ
There is nothing to be worried about, but feel free to give me feedback for further improvements!

Acknowledgments
I acknowledge the effort of Professor Agar for his dedication to teaching and designing such insightful and interesting projects.

Future Plans
I plan to develop the game environment at my earliest convenience to improve and gather all features for letting users control and play more easily with an extended GUI.
====

This project has been set up using PyScaffold 4.5. For details and usage
information on PyScaffold see https://pyscaffold.org/.
