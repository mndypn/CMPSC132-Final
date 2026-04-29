import random

class NumberGuessingGame:
    def __init__(self, low=1, high=100):
        self.low = low
        self.high = high
        self.target = random.randint(low, high)
        self.attempts = 0

    def get_guess(self):
        user_input = input(f"Guess a number ({self.low}-{self.high}): ").strip()

        if not user_input.isdigit():
            print("Invalid input. Please enter an integer.")
            return None

        guess = int(user_input)

        if guess < self.low or guess > self.high:
            print(f"Out of range. Enter a number between {self.low} and {self.high}.")
            return None
        return guess

    def evaluate_guess(self, guess):
        self.attempts += 1
        if guess == self.target:
            print(f"Correct! You guessed it in {self.attempts} attempts!")
            return True
        elif guess < self.target:
            print("Too low, guess a higher number")
        else:
            print("Too high, guess a lower number")
        return False


def ask_replay():
    valid = False
    answer = ""
    while not valid:
        answer = input("Play again? (y/n): ").strip().lower()
        if answer == "y" or answer == "n":
            valid = True
        else:
            print("Please enter 'y' or 'n'.")
    return answer == "y"

def main():
    playing = True
    attempts_history = []
    while playing:
        game = NumberGuessingGame()
        game_over = False
        print("New game started.")
        while not game_over:
            guess = game.get_guess()
            if guess is not None:
                game_over = game.evaluate_guess(guess)
        attempts_history.append(game.attempts)
        best_attempts = min(attempts_history)
        print(f"Attempts this round: {game.attempts}\nBest attempt: {best_attempts}")

        playing = ask_replay()
    print("Thanks for playing.")


main()