from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank =[]
for quest_data in question_data:
    question = Question(quest_data["question"],quest_data["correct_answer"])
    question_bank.append(question)

quizbrain = QuizBrain(question_bank)
while quizbrain.still_has_questions():
    quizbrain.next_question()

print("You've completed the quiz.")
print(f"Your final score is {quizbrain.score}/{quizbrain.question_number}")

