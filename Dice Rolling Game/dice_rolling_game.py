import random

def get_dice_number():
    while True:
        try:
            #Ask the user for the no of dice
            dice_number = int(input("How many dice do you want to roll?\n"))

            #check for edge cases
            if dice_number <= 0:
                print("Enter a number greater than zero.")
            elif dice_number > 10:
                print("Maximum number of dice is 10")
            else:
                return dice_number
            
        except ValueError:
            print("Please Enter a Valid input")

def roll_dice(n):
    return tuple(random.randint(1,6) for _ in range(n))

def main():
    print("Welcome to Dice Rolling Game!")

    dice_number = get_dice_number()

    #loop until exit(inp make sure it has a break condition)
    while True:

        #Ask the user for a input
        user_input = input("Do you want to roll the dice? (y/n): ").strip().lower()

        #Check the input and check validity
        if user_input == "y":
            print(f"You Rolled: {roll_dice(dice_number)}")
        elif user_input == "n":
            print("Thank You for Playing.")
            break
        else:
            print("Invalid Input!")

if __name__ == "__main__":
    main()