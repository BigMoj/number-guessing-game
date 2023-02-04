import random


def check_answer(guess, answer, turns):
    if guess > answer:
        print("too high")
        return turns - 1
    elif guess < answer:
        print("too low")
        return turns - 1
    else:
        print(f"Correct! the answer was {answer}.")


def set_difficulty():
    level = input("choose the difficulty.type 'hard' or 'easy': ")
    if level == "easy":
        return 10
    elif level == "hard":
        return 5


def game():
    answer = random.randint(1, 100)
    print(answer)
    print("welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts remain.")
        guess = int(input("make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("you are out of guess, you loose")
            return


game()