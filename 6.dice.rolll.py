import random
import os
import sys

# Define ASCII art for each side of the die
DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
}

def clear_console():
    """Clears the console for better readability."""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:                # For Linux and Mac
        os.system('clear')

def roll_die():
    """Rolls the die and returns a random number between 1 and 6."""
    return random.randint(1, 6)

def display_die(number):
    """Displays the ASCII art for the rolled die number."""
    die_art = DICE_ART.get(number)
    if die_art:
        for line in die_art:
            print(line)
    else:
        print("Invalid die number.")

def main():
    """Main function to run the dice roll program."""
    while True:
        input("Press Enter to roll the die...")
        clear_console()
        result = roll_die()
        print(f"You rolled a {result}!\n")
        display_die(result)
        print("\nDo you want to roll again? (y/n): ", end='')
        choice = input().strip().lower()
        if choice != 'y':
            print("Thanks for playing!")
            break
        clear_console()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user. Goodbye!")
        sys.exit()
