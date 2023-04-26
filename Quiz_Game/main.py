from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for each_question in question_data:
    q_text = each_question["text"]
    q_ans = each_question["answer"]
    question_bank.append(Question(q_text,q_ans))

quix = QuizBrain(question_bank)

while quix.still_has_question():
    quix.next_question()





