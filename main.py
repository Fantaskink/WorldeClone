#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    dune_mode = False

    discarded_letters = set()
    solution = get_random_solution(dune_mode)
    #print(solution)

    guess = ""
    number_of_guesses = 0

    while guess != solution:
        guess = prompt_player_word(solution)
        number_of_guesses += 1
        discarded_letters.update(analyse_guess(guess, solution))
        print("Discarded letters: ")
        for element in discarded_letters:
            print(element, end=", ")
        print()

        print("Guesses left: " + str(6 - number_of_guesses))


def get_random_solution(dune_mode):
    import random

    if dune_mode:
        with open('words/dune_solutions.csv', 'r') as f:
            dune_solutions = f.read().splitlines()
            return random.choice(dune_solutions)

    with open('words/valid_solutions.csv', 'r') as f:
        valid_solutions = f.read().splitlines()
        return random.choice(valid_solutions)


def prompt_player_word(solution):
    solution_length = len(solution)
    player_input = input("Enter a word with " + str(solution_length) + " letters: ")

    if not player_input.isalpha() or len(player_input) != solution_length:
        print("Invalid input.")
        return prompt_player_word(solution)

    return player_input


def analyse_guess(guess, solution):
    solution_length = len(solution)
    output = ""
    letters = []
    discarded_letters = set()
    for i in range(0, solution_length):
        letters.append(guess[i])

    for i in range(0, solution_length):
        if guess[i] == solution[i]:
            output += "🟩"
            letters.remove(guess[i])
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
