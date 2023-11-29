from player import Player, PlayerTurn
from colorama import Fore, Style
import pyfiglet
from termcolor import colored
from Ai_Player import PlayerTurn_ai
def generate_block_art():
    art = """
  _____          __  __ ______    ______      ________ _____  
 / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ 
| |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
| | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
| |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
 \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\
    """
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
    color_index = 0
    for line in art.split('\n'):
        for char in line:
            if char != ' ':
                print(colors[color_index % len(colors)] + char, end='')
                color_index += 1
            else:
                print(' ', end='')
        print()
# while loop for replayability
play_again = True
while play_again:
    num_players=[]
    # global initial_cal
    print("---------------------------------------------------------------")  
    num_players = int(input("Enter the number of players including Ai player: "))
    # num_players =num_players +1
    All_names = []
    Save_initial = []
    All_names = []
    player =[]
    All_names=[]
    player_scores = [[] for i in range(num_players)]
    player_scores_details = [[] for i in range(num_players)]


    # Gather names of each player
    for i in range(num_players):

            player = Player()
            All_names.append(player.get_name())

    # For each player, run their turn and store their scores
    player_scores = [["" for i in range(14)] for j in range(num_players)]
    player_scores_details = [[] for j in range(num_players)]

    for j in range(13):
        for i in range(num_players):

            initial_cal = player_scores[i]
            print("--------------------------------------------------------------------------------------")  
            
            if i==0:

                
                player_turn = PlayerTurn_ai(initial_cal)
                total_score = player_turn.get_total_score()
                updated_matrix = player_turn.get_updated_matrix()            
            else: 
                # print(initial_cal)
                print(f"Player {i + 1}: {All_names[i]}")
                player_turn = PlayerTurn(initial_cal)
                total_score = player_turn.get_total_score()
                updated_matrix = player_turn.get_updated_matrix()
                print("--------------------------------------------------------------------------------------")  
 
                print(f"| {All_names[i]}                           |     The total score for {All_names[i]} is:   {total_score}   |")
  
            # player_scores.append((total_score,updated_matrix))

            player_scores[i].append(updated_matrix)
            player_scores_details[i].append(total_score)
    all_final_score=[]
    # Display results for each player
    for i, name in enumerate(All_names):
        updated_matrix = player_scores[i]
        total_sc = player_scores_details[i][-1]
        all_final_score.append(total_sc)
    # Finding the maximum score   
    max_score = max(all_final_score)  
    max_index = all_final_score.index(max_score)
    generate_block_art()
    print("---------------------------------------------------------------")
    # Select a font (you can choose from different fonts available in pyfiglet)
    font = "slant"  
    # Generate ASCII art based on user input, using the chosen font

    max_element = max(all_final_score)
    if all_final_score.count(max_element) == 1:
        ascii_art = pyfiglet.figlet_format(f"Congratulations {All_names[max_index]}", font=font)

        print (f"{All_names[max_index]}  win the game with {max_score} points")
        print("---------------------------------------------------------------")
    else:
        ascii_art = pyfiglet.figlet_format("Tie", font=font)

    # Print the ASCII art with color
    colored_ascii_art = colored(ascii_art, color="green")  # Change color as needed
    print(colored_ascii_art)
   
    print("---------------------------------------------------------------")
    for i, name in enumerate(All_names):
        print(f"[Player {i + 1}: {name}  ===>  Total Score: {all_final_score[i]}]")
        print("---------------------------------------------------------------")
    replay_input = input("Do you want to play again? (yes/no): ")
    if replay_input.lower() != 'yes':
        play_again = False
    else:
        player_id=0