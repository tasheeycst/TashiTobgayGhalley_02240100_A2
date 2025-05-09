class PokemonCardBinderManager:
    """Manages a Pokémon card binder with functions to add, reset, view, and exit."""

    def __init__(self):
        """Initializes an empty binder dictionary."""
        self.binder = {}  # {pokedex_number: (page, row, column)}

    def add_card(self):
        """Adds a Pokémon card by Pokedex number with validation and position logic."""
        try:
            pokedex = int(input("Enter Pokedex number (1–1025): "))
            if not (1 <= pokedex <= 1025):
                print(" Invalid Pokedex number. Must be between 1 and 1025.")
                return
        except ValueError:
            print(" Invalid input. Please enter a valid integer.")
            return

        if pokedex in self.binder:
            page, row, col = self.binder[pokedex]
            print(f" Card already exists.\n Page: {page}, Position: ({row},{col})\nStatus: Duplicate")
        else:
            index = len(self.binder)
            page = index // 64 + 1
            position = index % 64
            row = position // 8 + 1
            col = position% 8 + 1
            self.binder[pokedex] = (page, row, col)
            print(f"Card added.\nPage: {page}, Position: ({row},{col})\nStatus: Added")

    def reset_binder(self):
        """Resets the binder after user confirms action."""
        print("WARNING: This will erase all cards in the binder.")
        choice = input("Type 'CONFIRM' to proceed or 'EXIT' to cancel: ").strip().upper()
        if choice == "CONFIRM":
            self.binder.clear()
            print(" Binder has been reset.")
        elif choice == "EXIT":
            print("Reset cancelled.")
        else:
            print(" Invalid choice. Reset not performed.")

    def display_binder(self):
        """Displays all stored cards and completion percentage."""
        print("Current Binder Summary")
        if not self.binder:
            print(" Binder is empty.")
        else:
            sorted_cards = sorted(self.binder.items())
            for pokedex, (page, row, col) in sorted_cards:
                print(f"Pokedex #{pokedex} ➡ Page: {page}, Position: ({row},{col})")
            total = len(self.binder)
            completion = (total / 1025) * 100
            print(f"Total cards: {total}")
            print(f"Completion: {completion:.2f}%")

    def exit_session(self):
        """Displays a summary and exits the session."""
        print(f"Exiting binder. Total cards stored: {len(self.binder)}")
        return len(self.binder)

    def menu(self):
        """Runs the binder manager menu loop until user chooses to exit."""
        while True:
            print("Pokemon Card Binder Manager")
            print("1. Add a Pokemon card by Pokedex number")
            print("2. Reset the Binder")
            print("3. Display current cards and stats")
            print("4. Exit to Main Menu")
            mode = input("Select a mode (1-4): ").strip()

            if mode == '1':
                self.add_card()
            elif mode == '2':
                self.reset_binder()
            elif mode == '3':
                self.display_binder()
            elif mode == '4':
                score = self.exit_session()
                return score
            else:
                print("Invalid option. Please enter a number between 1 and 4.")
