from question_model import question
from data import question_data
from quiz_brain import Quiz_Brain
question_bank = []
for x in question_data:
    question_bank.append(question(x["question"], x["correct_answer"]))

quiz = Quiz_Brain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
