class Question:
    def __init__(self, text, options, answer, prize):
        self.text = text
        self.options = options
        self.answer = answer
        self.prize = prize

    # def display_question(self):
    #     print(f"\nPrize: ₹{self.prize}\n")
    #     print(self.text)

    #     for index, option in enumerate(self.options, start=1):
    #         print(f"{index} : {option}")

    def check_answer(self, user_input):
        return user_input == self.answer