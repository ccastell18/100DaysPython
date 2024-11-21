from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(answer=question_answer, text=question_text)
    questions_bank.append(new_question)

quiz = QuizBrain(questions_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your score is {quiz.score}/{quiz.question_number}")
