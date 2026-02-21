import random

def get_range():
    while True:
        try:
            print("Choose the range of numbers")
            min_range = int(input("Enter the min range: "))
            max_range = int(input("Enter the max range: "))

            if min_range > max_range:
                print("The minimum cannot be greater than the max")
            else:
                return min_range, max_range
                
        except ValueError:
            print("Invalid input")

def generate_number(min_range, max_range):
    return random.randint(min_range,max_range)

def play_round(n, life, score):
    while life > 0:
        try:
            guess = int(input("Your guess: "))

            if guess < n:
                print("Too Low!")
                life -= 1
                print(f"Life remaining: {life}")
            elif guess > n:
                print("Too High!")
                life -= 1
                print(f"Life remaining: {life}")
            else:
                print("Congratulations! You guessed the number.")
                score += 1
                print(f"Your score is {score}")
                return life, score

        except ValueError:
            print("Please enter a valid number.")

    print("Game Over!")
    print(f"The correct answer was {n}")
    return life, score

def ask_replay():
    while True:
        try:
            user_input = input(" Do you want to Try Again? y/n : ").strip().lower()

            if user_input in ["y", "yes"]:
                return True
            elif user_input in ["n","no"]:
                print("Thank You for playing.")
                return False
            else:
                print("Invalid Input.")
        except ValueError:
            print("Invalid Input")

def main():
    score = 0

    while True:

        life = 10

        min_range, max_range = get_range()

        rand_number = generate_number(min_range,max_range)

        print(f"Guess the number between {min_range} and {max_range}: ")

        life, score = play_round(rand_number,life, score)

        if not ask_replay():
            break

if __name__ == "__main__":
    main()