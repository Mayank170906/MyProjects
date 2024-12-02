class QuizBrain:
    def __init__(self, q_list):
        self.q_no = 0
        self.question_list = q_list
        self.score = 0

    def ask(self):
        print("Let's begin the quiz")
        while self.q_no < len(self.question_list):
            current_question = self.question_list[self.q_no]
            user = input(
                f"no.{self.q_no} {current_question.text} True/False\n:")
            if user == current_question.answer:
                self.score += 1
                print(
                    f"You are correct answer would be {current_question.answer}")
            else:
                print(
                    f"You are wrong answer would be {current_question.answer}")
            self.q_no += 1
        print("Congratulations you had completed the quiz.")
        print(f"Your score is {self.score}")
