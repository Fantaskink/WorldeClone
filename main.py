#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    solution = get_random_solution()
    print(solution)
    guess = prompt_player_word()
    analyse_guess(guess, solution)


def get_random_solution():
    import random

    with open('words/valid_solutions.csv', 'r') as f:
        valid_solutions = f.read().splitlines()
        return random.choice(valid_solutions)


def prompt_player_word():
    player_input = input("Enter a word: ")

    if not player_input.isalpha() or len(player_input) != 5:
        print("Invalid input.")
        return prompt_player_word()

    return player_input


def analyse_guess(guess, solution):
    output = ""
    for i in range(0,5):
        if guess[i] == solution[i]:
            output += "🟩"
        elif guess[i] in solution:
            output += "🟨"
        else:
            output += "⬜"

    print(output)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
