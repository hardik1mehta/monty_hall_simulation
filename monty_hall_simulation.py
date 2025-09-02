# ... existing code ...
# Bug fix MHS-8: Verified the calculation logic is correct.
switched_choice = random.choice(available_switch_doors)
# ... existing code ...
import random

def run_simulation(num_doors, num_simulations):
    """
    Runs the Monty Hall simulation for a given number of doors and simulations.

    Args:
        num_doors (int): The total number of doors in the game (e.g., 3 or 4).
        num_simulations (int): The number of times to run the simulation (e.g., 10000).

    Returns:
        tuple: A tuple containing the win percentage for switching and not switching.
    """
    switch_wins = 0
    stay_wins = 0

    for _ in range(num_simulations):
        # Setup the game
        # Doors are represented by numbers from 0 to num_doors-1
        prize_door = random.randint(0, num_doors - 1)
        player_choice = random.randint(0, num_doors - 1)

        # Monty opens a door
        doors_to_open = []
        for i in range(num_doors):
            # Monty can't open the prize door or the player's choice
            if i != prize_door and i != player_choice:
                doors_to_open.append(i)
        
        # In the 3-door problem, Monty opens one door.
        # In the 4-door problem, the problem statement says he still opens only one.
        monty_opens = random.choice(doors_to_open)

        # Player decides to switch or stay

        # --- Case 1: Player Stays ---
        if player_choice == prize_door:
            stay_wins += 1

        # --- Case 2: Player Switches ---
        # The player must switch to a door that is not their original choice
        # and not the one Monty opened.
        available_switch_doors = []
        for i in range(num_doors):
            if i != player_choice and i != monty_opens:
                available_switch_doors.append(i)
        
        switched_choice = random.choice(available_switch_doors)

        if switched_choice == prize_door:
            switch_wins += 1

    # Calculate percentages
    switch_win_percentage = (switch_wins / num_simulations) * 100
    stay_win_percentage = (stay_wins / num_simulations) * 100

    return switch_win_percentage, stay_win_percentage

def main():
    """
    Main function to run the simulations and print the results.
    """
    num_simulations = 10000

    print("--- Monty Hall Problem Simulation ---")
    print(f"Running {num_simulations} simulations for each scenario.\n")

    # Part (a): 3-Door Problem
    print("--- Scenario 1: 3 Doors ---")
    three_door_switch, three_door_stay = run_simulation(3, num_simulations)
    print(f"Win percentage by SWITCHING: {three_door_switch:.2f}%")
    print(f"Win percentage by NOT SWITCHING: {three_door_stay:.2f}%")
    print("-" * 30 + "\n")

    # Part (b): 4-Door Problem
    print("--- Scenario 2: 4 Doors ---")
    four_door_switch, four_door_stay = run_simulation(4, num_simulations)
    print(f"Win percentage by SWITCHING: {four_door_switch:.2f}%")
    print(f"Win percentage by NOT SWITCHING: {four_door_stay:.2f}%")
    print("-" * 30)

if __name__ == "__main__":
    main()
    