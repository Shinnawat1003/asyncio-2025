import time
from datetime import timedelta

speed = 1 #speed
JUDIT_TIME = 5 / speed # Judit time move
OPPONENT_TIME = 55 / speed # Opponent time move
opponents = 24 # Number of opponents
move_pairs = 30 # Number of move pairs
JITTER = 24.6  # Jitter time in seconds

def play_game(board_id): # Function to simulate a game on a chess board
    calculated_time = (JUDIT_TIME + OPPONENT_TIME) * move_pairs 
    real_time = calculated_time + JITTER  
    
    for i in range(1, move_pairs + 1): # Loop through each move pair
        print(f"BOARD-{board_id} {i} Judit made a move with {int(JUDIT_TIME)} secs.") 
        print(f"BOARD-{board_id} {i} Opponent made move with {int(OPPONENT_TIME)} secs.") 

    print(f"BOARD-{board_id} – >>>>>>>>>>>>>>> Finished move in {real_time:.1f} secs") 
    print(f"BOARD-{board_id} – >>>>>>>>>>>>>>> Finished move in {calculated_time:.1f} secs (calculated)\n") 

    return real_time, calculated_time 

def main(): # Main function to run the chess game simulation
    print(f"Number of games: {opponents} games.") 
    print(f"Number of move: {move_pairs} pairs.") 

    real_time, calculated_time = play_game(1) 
    # Convert seconds to timedelta for better readability
    delta_real = timedelta(seconds=real_time) 
    delta_calc = timedelta(seconds=calculated_time) 
    # Format the output for real and calculated times
    real_str = str(delta_real).split(".")[0] 
    calc_str = str(delta_calc).split(":") 
    calc_hr = f"{int(calc_str[0])}:{calc_str[1]}" 

    print(f"Board exhibition finished for 1 opponents in {real_str} hr.") 
    print(f"Board exhibition finished for 1 opponents in {calc_hr} hr.  (calculated)") 

main()