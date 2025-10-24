import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def select(title: str, choices: list[str], clear_screen_after=True) -> str:
    # print ui
    print(title)
    for i, choice in enumerate(choices):
        print(f"{i+1} - {choice}")

    # input logic
    max_valid_choice = len(choices)
    while True:
        choice = input("Enter: ")
        if choice.isdigit() and int(choice) in range(1, max_valid_choice + 1):
            if clear_screen_after:
                clear_screen()
            return choice


def input_float(prompt: str) -> float:
    while True:
        return_value = input(prompt)
        try:
            return float(return_value)
        except ValueError:
            print("Invalid float number.")


def input_int(prompt: str) -> int:
    while True:
        return_value = input(prompt)
        if return_value.isdigit():
            return int(return_value)
        else:
            print("Invalid integer.")


def input_bool(prompt: str) -> bool:
    while True:
        return_value = input(prompt).lower()
        if return_value in ["y", "n"]:
            return return_value == "y"
        else:
            print("Invalid choice.")
