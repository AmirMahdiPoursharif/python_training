import random

from .winner_logic import select_winner

def main():
    choices = {
        1: "🪨",
        2: "📃",
        3: "✂"
    }
    print("***    rock paper scissors    ***")
    print(f"The selections are:\n1 - rock/🪨\n2 - paper/📃\n3 - scissors/✂")

    cpu_choice : int = random.randint(1, 3)
    human_choice : int = int(input("please enter your choice from 1 to 3: "))

    winner = select_winner(cpu_choice, human_choice)

    if winner == cpu_choice:
        return f"cpu won the game\ncpu choice: {choices[cpu_choice]}, human choice: {choices[human_choice]}"
    elif winner == human_choice:
        return f"human won the game\ncpu choice: {choices[cpu_choice]}, human choice: {choices[human_choice]}"
    else:
        return f"Equal\ncpu choice: {choices[cpu_choice]}, human choice: {choices[human_choice]}"


if __name__ == '__main__':
    print(main())
