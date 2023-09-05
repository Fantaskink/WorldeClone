#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    discarded_letters = set()
    solution = get_random_solution()
    print(solution)

    guess = ""
    number_of_guesses = 0

    while guess != solution:
        guess = prompt_player_word()
        number_of_guesses += 1
        discarded_letters.update(analyse_guess(guess, solution))
        print("Discarded letters: ")
        for element in discarded_letters:
            print(element, end=", ")
        print()

        print("Guesses left: " + str(6 - number_of_guesses))


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
    letters = []
    discarded_letters = set()
    for i in range(0, 5):
        letters.append(guess[i])

    for i in range(0,5):
        if guess[i] == solution[i]:
            output += "🟩"
        elif guess[i] in solution and guess[i] in letters:
            output += "🟨"
            letters.remove(guess[i])
        else:
            output += "⬜"
            discarded_letters.add(guess[i])

    print(output)

    return discarded_letters


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
