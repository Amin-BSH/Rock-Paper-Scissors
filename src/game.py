import random
from typing import List


class RockPaperScissors:
    """
    A simple Rock-Paper-Scissors game.

    Attributes:
        movements (list): List of possible moves (rock, paper, scissors).
        your_score (int): Player's score.
        computer_score (int): Computer's score.
    """

    def __init__(self) -> None:
        """
        Initializes the game with default scores and movement options.
        """
        self.movements: List["str"] = ["rock🪨", "paper📖", "scissors✂️"]
        self.your_score: int = 0
        self.computer_score: int = 0

    def your_choice(self) -> int:
        """
        Asks the player for their choice and returns it.

        Returns:
            int: The player's choice (1 for rock, 2 for paper, 3 for scissors).
        """
        self.print_movements()
        choice = int(input("What is your choice? "))
        if choice not in [1, 2, 3]:
            print("You have entered a wrong number! Try again.")
            return self.your_choice()
        else:
            return choice

    def computer_choice(self) -> int:
        """
        Generates a random computer choice.

        Returns:
            int: The computer's choice (1 for rock, 2 for paper, 3 for scissors).
        """
        choices: List[int] = [1, 2, 3]
        return random.choice(choices)

    def print_movements(self) -> None:
        """
        Prints the available movement options.
        """
        print("Choose your move:")
        for index, elem in enumerate(self.movements, 1):
            print(f"• {index}: {elem}")

    def score(self, y_choice: int, c_choice: int) -> None:
        """
        Computes the score based on player and computer choices.

        Args:
            y_choice (int): Player's choice (1 for rock, 2 for paper, 3 for scissors).
            c_choice (int): Computer's choice (1 for rock, 2 for paper, 3 for scissors).
        """
        if y_choice == c_choice:
            pass
        elif (
            (y_choice == 1 and c_choice == 2)
            or (y_choice == 2 and c_choice == 3)
            or (y_choice == 3 and c_choice == 1)
        ):
            self.computer_score += 1
        else:
            self.your_score += 1

    def show_score(self) -> None:
        """
        Displays the current scores.
        """
        print("-" * 30)
        print(
            f" Your score: {self.your_score} | Computer's score: {self.computer_score} "
        )
        print("-" * 30)

    def show_decision(self, y_choice: int, c_choice: int) -> None:
        """
        Displays the player's and computer's choices.

        Args:
            y_choice (int): Player's choice (1 for rock, 2 for paper, 3 for scissors).
            c_choice (int): Computer's choice (1 for rock, 2 for paper, 3 for scissors).
        """
        print("-" * 30)
        print(
            f" Your choice: {self.movements[y_choice - 1]} | Computer's choice: {self.movements[c_choice - 1]} "
        )
        print("-" * 30)

    def winner(self) -> None:
        """
        Determines and displays the winner of the game.
        """
        if self.your_score == self.computer_score:
            print("It's a draw! 🤝")
            self.show_score()
        elif self.your_score > self.computer_score:
            print("🏆" * 10, " You won! ", "🏆" * 10)
            self.show_score()
        else:
            print("😭" * 10, " You lost! ", "😭" * 10)
            self.show_score()

    def play(self) -> None:
        """
        Main method to play Rock, Paper, Scissors
        Gets the player's choice, computes the winner, and updates scores.
        """
        y_choice = self.your_choice()
        c_choice = self.computer_choice()
        if y_choice and c_choice:
            self.score(y_choice=y_choice, c_choice=c_choice)
            self.show_decision(y_choice=y_choice, c_choice=c_choice)


if __name__ == "__main__":
    while True:
        game = RockPaperScissors()
        for _ in range(3):
            game.play()
        game.winner()

        if (
            input(
                "Do you want to play again? (Enter any key to continue or 'q' to quit): "
            ).lower()
            == "q"
        ):
            print("See you later!")
            break
