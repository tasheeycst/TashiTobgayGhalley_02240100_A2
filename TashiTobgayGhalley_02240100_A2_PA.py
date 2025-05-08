import random
import TashiTobgayGhalley_02240100_A2_PB 
class Game:
    def __init__(self):
        pass
    def display_menu(self):
        print("Main Menu")
        print("1. Guess Number Game")
        print("2. Rock Paper Scissors")
        print("3. Trivia Pursuit Quiz")
        print("4. Pokemon Card Binder Manager")
        print("5. Exit")

    def start(self):

        while True:
            self.display_menu()
            choice = input("Select a function (1-6): ")
            if choice == '1':
                GuessNumberGame().play()
            elif choice == '2':
                RockPaperScissors().play()
            elif choice == '3':
                TriviaGame().play()
            elif choice == '4':
                TashiTobgayGhalley_02240100_A2_PB. PokemonCardBinderManager().menu()
            elif choice == '5':
                print("Thanks for playing!")
                break
            else:
                print("Invalid choice. Try again.")

class GuessNumberGame:
    def play(self):
        number = random.randint(1, 20)
        score = 0
        guesses = 0
        print("Guess a number between 1 and 20 : ")
        while True:
            guess = int(input("Your guess: "))
            guesses += 1
            if guess == number:
                print("Correct!")
                break
            elif guess < number:
                print("Too low.")
            else:
                print("Too high.")
            
        score = max(0, 10 - (guesses - 1))
        print(f"Score: {score}")
        return score

class RockPaperScissors:
    def play(self):
        options = ['rock', 'paper', 'scissors']
        score = 0
        print("Play Rock Paper Scissors. Type 'exit' to quit :")
        while True:
            user = input("Your choice (rock/paper/scissors): ").lower()
            if user == 'exit':
                break
            if user not in options:
                print("Invalid input.")
                continue
            computer = random.choice(options)
            print(f"Computer chose: {computer}")
            if user == computer:
                print("It's a draw!")
            elif (user == 'rock' and computer == 'scissors') or \
                 (user == 'paper' and computer == 'rock') or \
                 (user == 'scissors' and computer == 'paper'):
                print("You win!")
                score += 1
            else:
                print("You lose.")
        print(f"Score: {score}")
        return score

class TriviaGame:
    def __init__(self):
        self.questions = {
            'Bhutanese Tradition :': [
                ("What is the national animal of Bhutan?", ['Cow', 'Yak', 'Takin', 'sheep'], 'Takin'),
                ("what is nation Bird in Bhutan?", ['Raven', 'Peacock', 'Hen', 'Crow'], 'Raven')
            ],
            'Mathematics :': [
                ("x=5y+1 Find Y if x = 11?", ['1', '3', '11', '2'], '2'),
                  ("1,2,4,7,11,x,22?", ['6', '12', '16', '18'], '16')
            ]
        }

    def play(self):
        score = 0
        print("Categories:\n1. ", "\n2.  ".join(self.questions.keys()))
        category = input("Choose a category: ").title()
        if category not in self.questions:
            print("Invalid category.")
            return 0
        for q, choices, correct in self.questions[category]:
            print(f"{q}")
            for i, choice in enumerate(choices):
                print(f"{i + 1}. {choice}")
            
            ans = int(input("Choose the answer (1-4): "))
            if choices[ans - 1] == correct:
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")
        print(f"Score: {score}")
        return score

if __name__ == "__main__":
    Game().start()
