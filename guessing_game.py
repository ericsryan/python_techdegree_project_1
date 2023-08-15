"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

import os
import random

def clear_screen():
    """Clear the screen for better readability."""
    os.system('cls' if os.name == 'nt' else 'clear')

def start_game():
    """Begin the game loop."""

    high_score = 0

    while True:
        # Start with a clear screen
        clear_screen() 

        # Welcome screen
        print("Welcome to the Number Guessing Game!")
        if high_score >= 1:
            print(f"The high score to beat is {high_score}.")
        else:
            print("Play a round to set the first high score!")

        # Generate a random number
        random_number = random.randint(1, 10)
        
        print("\nGuess a number from 1 to 10.")

        # Track total number of guesses
        number_of_guesses = 0

        # Start loop for guessing the number
        while True:
            # Make sure the number is an integer
            try:
                guessed_number = int(input("What is your guess? "))
            except ValueError:
                print("\nThat is not a valid number." +
                      "Please enter a number from 1 to 10.")
                continue
            # Make sure number is in range
            if guessed_number < 1 or guessed_number > 10:
                print("\nYour guess needs to be a number from 1 to 10.")
            elif random_number < guessed_number:
                print("\nIt's lower")
                number_of_guesses += 1
            elif random_number > guessed_number:
                print("\nIt's higher")
                number_of_guesses += 1
            elif random_number == guessed_number:
                print(f"\nThat's right! The answer was {guessed_number}!")
                number_of_guesses += 1
                break

        # End of round screen        
        print(f"\nYou guessed the number in {number_of_guesses} tries.")
        if high_score == 0 or number_of_guesses < high_score:
            high_score = number_of_guesses
        print(f"The high score is {high_score} guesses.")

        # Give player option to play again
        continue_game = input("\nPress [Enter] to try for a new high score " +
                              "or press 'q' then [Enter] to quit. ")
        if continue_game.lower() == 'q':
            print("\nThanks for playing! Bye!\n")
            break

if __name__ == '__main__':
    start_game()