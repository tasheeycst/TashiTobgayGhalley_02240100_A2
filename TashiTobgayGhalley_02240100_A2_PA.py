import random
import TashiTobgayGhalley_02240100_A2_PB

class Game:
    """Main game class to display menu and run selected games."""

    def __init__(self):
        self.total_score = 0  # Overall score tracker

    def display_menu(self):
        """Displays the main menu options."""
        print("\nMain Menu")
        print("1. Guess Number Game")
        print("2. Rock Paper Scissors")
        print("3. Trivia Pursuit Quiz")
        print("4. Pokemon Card Binder Manager")
        print("5. Show Overall Score")
        print("6. Exit")

    def start(self):
        """Starts the main game loop and handles user selection."""
        while True:
            self.display_menu()
            choice = input("Select a function (1-6): ")
            if choice == '1':
                self.total_score += GuessNumberGame().play()
            elif choice == '2':
                self.total_score += RockPaperScissors().play()
            elif choice == '3':
                self.total_score += TriviaGame().play()
            elif choice == '4':
                self.total_score += TashiTobgayGhalley_02240100_A2_PB.PokemonCardBinderManager().menu()
            elif choice == '5':
                print(f"Your Overall Score Across All Games: {self.total_score}")
            elif choice == '6':
                print("Thanks for playing!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

class GuessNumberGame:
    """Class for the number guessing game."""

    def play(self):
        """Plays the Guess Number Game with input validation and scoring."""
        number = random.randint(1, 100)
        score = 0
        guesses = 0
        print("Guess the Number (1 to 100)")
        while True:
            try:
                guess = int(input("Your guess: "))
                if guess < 1 or guess > 100:
                    print("Please enter a number between 1 and 100.")
                    continue
                guesses += 1
                if guess == number:
                    print("Correct!")
                    break
                elif guess < number:
                    print("Too low!.")
                else:
                    print("Too high!.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        score = max(0, 10 - (guesses - 1))
        print(f"Score: {score}")
        return score

class RockPaperScissors:
    """Class for the Rock Paper Scissors game."""

    def play(self):
        """Plays Rock Paper Scissors game in a loop until user exits."""
        options = ['rock', 'paper', 'scissors']
        score = 0
        print("Rock Paper Scissors")
        print("Type 'exit' to return to main menu.")
        while True:
            user = input("Your choice (rock/paper/scissors): ").lower()
            if user == 'exit':
                break
            if user not in options:
                print("Invalid input. Please type rock, paper, or scissors.")
                continue
            computer_choice = random.choice(options)
            print(f"Computer chose: {computer_choice}")
            if user == computer_choice:
                print("It's a draw!")
            elif (user == 'rock' and computer_choice == 'scissors') or \
                 (user == 'paper' and computer_choice == 'rock') or \
                 (user == 'scissors' and computer_choice == 'paper'):
                print("You win!")
                score += 1
            else:
                print("You lose.")
        print(f"Score: {score}")
        return score

class TriviaGame:
    """Class for Trivia Pursuit Game."""

    def __init__(self):
        self.questions = {
            'Bhutanese Tradition': [
                ("What is the national animal of Bhutan?", ['Cow', 'Yak', 'Takin', 'Sheep'], 'Takin'),
                ("What is the national bird of Bhutan?", ['Raven', 'Peacock', 'Hen', 'Crow'], 'Raven')
            ],
            'Mathematics': [
                ("x = 5y + 1. Find y if x = 11?", ['1', '3', '11', '2'], '2'),
                ("What number comes next: 1, 2, 4, 7, 11, x, 22?", ['6', '12', '16', '18'], '16')
            ]
        }

    def play(self):
        """Runs the trivia quiz game with category selection and question answering."""
        score = 0
        print("Trivia Pursuit Quiz")
        categories = list(self.questions.keys())
        for i, cat in enumerate(categories):
            print(f"{i + 1}. {cat}")
        try:
            selected = int(input("Choose a category (1-{}): ".format(len(categories))))
            if selected < 1 or selected > len(categories):
                print("Invalid category number.")
                return 0
        except ValueError:
            print("Invalid input. Please enter a number.")
            return 0

        category = categories[selected - 1]
        for a, choices, correct in self.questions[category]:
            print(f"\n{a}")
            for i, choice in enumerate(choices):
                print(f"{i + 1}. {choice}")
            try:
                Answer = int(input("Choose the answer (1-4): "))
                if Answer < 1 or Answer > 4:
                    print("Invalid option. Skipping question.")
                    continue
                if choices[Answer - 1] == correct:
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        print(f"Score: {score}")
        return score

if __name__ == "__main__":
    Game().start()
