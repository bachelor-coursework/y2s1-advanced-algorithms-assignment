import os


def _clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def select(title: str, choices: list[str], clear_screen=True) -> str:
    # print ui
    print(title)
    for i, choice in enumerate(choices):
        print(f"{i+1} - {choice}")

    # input logic
    max_valid_choice = len(choices)
    while True:
        choice = input("Enter: ")
        if choice.isdigit() and int(choice) in range(1, max_valid_choice + 1):
            if clear_screen:
                _clear_screen()
            return choice
