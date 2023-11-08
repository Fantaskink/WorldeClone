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
    print(solution)

    guess = ""
    number_of_guesses = 0

    while guess != solution and number_of_guesses < 6:
        guess = prompt_player_word(solution, dune_mode)
        number_of_guesses += 1
        discarded_letters.update(analyse_guess(guess, solution))
        print("Discarded letters: ")

        for element in discarded_letters:
            print(element, end=", ")
        print()
        print("Guesses left: " + str(6 - number_of_guesses))

    if number_of_guesses < 6:
        print("You won!")
    else:
        print("You lost!")
        print("The solution was: " + solution)


def get_random_solution(dune_mode):
    import random

    if dune_mode:
        with open('words/dune_solutions.csv', 'r') as f:
            dune_solutions = f.read().splitlines()
            return random.choice(dune_solutions)

    with open('words/valid_solutions.csv', 'r') as f:
        valid_solutions = f.read().splitlines()
        return random.choice(valid_solutions)


def get_valid_guesses():
    with open('words/valid_guesses.csv', 'r') as f:
        valid_guesses = f.read().splitlines()
        return valid_guesses


def get_solutions():
    with open('words/valid_solutions.csv', 'r') as f:
        valid_solutions = f.read().splitlines()
        return valid_solutions


def prompt_player_word(solution, dune_mode):
    solution_length = len(solution)
    player_input = input("Enter a word with " + str(solution_length) + " letters: ")

    if not player_input.isalpha() or len(player_input) != solution_length:
        print("Invalid input.")
        return prompt_player_word(solution, dune_mode)

    if not dune_mode:
        valid_guesses = get_valid_guesses()
        valid_solutions = get_solutions()

        is_valid_guess = False

        if player_input in valid_guesses or player_input in valid_solutions:
            is_valid_guess = True

        if not is_valid_guess:
            print("Not a word")
            return prompt_player_word(solution, dune_mode)

    return player_input


def analyse_guess(guess, solution):
    solution_length = len(solution)
    output = ["_" for _ in range(solution_length)]
    letters = []
    discarded_letters = set()
    for i in range(0, solution_length):
        letters.append(solution[i])

    for i in range(0, solution_length):
        if guess[i] in solution and guess[i] in letters and guess[i] != solution[i]:
            output[i] = "🟨"
            letters.remove(guess[i])
        elif guess[i] == solution[i]:
            output[i] = "🟩"
            letters.remove(guess[i])
        else:
            output[i] = "⬜"
            if guess not in solution:
                discarded_letters.add(guess[i])

    output_string = ""
    for letter in output:
        output_string += letter
    print(output_string)

    return discarded_letters


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
