from enum import Enum


class Level(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3


def print_levels() -> None:
    """Prints available levels."""
    for level in Level:
        print(f"– {level.name} ({level.value})")
    print()


def print_welcome_msg() -> None:
    """Prints welcome message."""
    print("\nWelcome!\n")
    print("Choose difficulty:")
    print_levels()
    print('To exit, type "exit"\n')


def choose_level() -> int:
    """Prompts the user to input a difficulty level

    Returns:
            int: the level chosen
    """

    while True:
        inp = input("> ")
        if inp == "exit":
            exit()
        try:
            choice = int(inp)
        except ValueError:
            print("\nPlease, enter a digit.")
            print('To exit, type "exit"\n')
            continue
        if choice in Level:
            print(f"\nLevel chosen: {Level(choice).name}\n")
            return choice
        else:
            print("\nLevels available: ")
            print_levels()
