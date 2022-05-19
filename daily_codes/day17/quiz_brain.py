class Quiz_Brain:

    def __init__(self, question):
        self.question_number = 0
        self.question_list = question
        self.ans = ""
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]

        self.question_number += 1
        self.ans = input(f"Q.{self.question_number}: {current_question.text}(True/False)?: ")
        self.check_answer(current_question.answer)

    def check_answer(self, correct_ans):

        if self.ans.lower() == correct_ans.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong!")

        print(f"The correct answer is {correct_ans}")
        print(f"Your current score is: {self.score}/{self.question_number}.\n")

    def still_has_question(self):
        return self.question_number < len(self.question_list)