import random

ROCK = "r"
PAPER = "p"
SCISSOR = "s"

#check valid input
def user_input(choice):
    while True:
        user_choice = input("Rock 🪨, Paper 📃 or Scissors ✂️ : (r/p/s) ").strip().lower()
        if user_choice in choice:
            return user_choice
        else:
            print("Please enter a proper input!")

#generate random output
def rps_game(choice):
    return random.choice(choice)

#play game
def game(names, user_choice, computer_choice, win, score, rounds_played):
        print(f"You choose: {names[user_choice]}")
        print(f"Your opponent chose: {names[computer_choice]}")

        if user_choice == computer_choice:
            print("Tie")
            rounds_played += 1
            print(f"Score: {score}/{rounds_played}")
            return score, rounds_played
        elif win[user_choice] == computer_choice:
            print("You Win!")
            score += 1
            rounds_played += 1
            print(f"Score: {score}/{rounds_played}")
            return score, rounds_played
        else:
            print("You Lose!")
            score -= 1
            rounds_played += 1
            print(f"Score: {score}/{rounds_played}")
            return score, rounds_played

#ask replay
def play_again():
    while True:
        choice = input("Do you want to continue? (y/n): ").lower().strip()
        if choice in ["y", "yes"]:
            return True
        elif choice in ["n", "no"]:
            print("Thank you for playing!")
            return False
        else:
            print("Invalid Input!")

#main
def main():
    print("Welcome to Rock, Paper, Scissor Game!")

    names = {ROCK: "Rock 🪨", PAPER: "Paper 📃", SCISSOR: "Scissors ✂️"}
    choice = tuple(names.keys())
    win_con = {ROCK : SCISSOR, PAPER : ROCK, SCISSOR: PAPER}

    score = 0
    rounds_played = 0

    while True:
        user_choice = user_input(choice)
        computer_choice = rps_game(choice)

        score, play = game(names, user_choice,computer_choice,win_con,score,rounds_played)

        if not play_again():
            print(f"Your score is: {score}/{rounds_played}")
            break

if __name__ == "__main__":
    main()