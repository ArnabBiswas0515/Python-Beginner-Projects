from questions_data import questions

class MillionaireGame:
    def __init__(self, questions):
        self.questions = questions
        self.current_index = 0
        self.current_prize = 0
        self.game_over = False

    def get_current_question(self):
        if self.current_index < len(self.questions):
            return self.questions[self.current_index]
        return None
    
    def submit_answer(self, answer):
        question = self.get_current_question()

        if question.check_answer(answer):
            self.current_prize = question.prize
            self.current_index += 1
            return {
                "status" : True,
                "prize" : self.current_prize
            }
        else:
            self.game_over = True
            return {
                "status" : False,
                "prize" : self.current_prize
            }

    def get_question_data(self):
        question = self.get_current_question()

        if not question:
            return None

        return {
            "text": question.text,
            "options": question.options
        }

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

def run_cli():

    print("Welcome To Who Wants To Be A Millioniare")

    while True:
        game = MillionaireGame(questions)

        while not game.game_over:
            question = game.get_current_question()

            if question is None:
                print(f"Congratulations! You won ₹{game.current_prize}")
                break

            data = game.get_question_data()

            print(data["text"])
            for i, option in enumerate(data["options"], start=1):
                print(f"{i}. {option}")

            try:
                user_input = int(input("Enter your answer (1-4): "))
            except ValueError:
                print("Invalid Input. Game Over")
                break

            result = game.submit_answer(user_input)

            if result["status"] == True:
                print("\nCorrect!\n")
                print(f"Prize: ₹{game.current_prize}\n")
            else:
                print("Wrong answer!")
                print(f"You won ₹{result['prize']}")
                break

        if not ask_replay():
            break

if __name__ == "__main__":
    run_cli()