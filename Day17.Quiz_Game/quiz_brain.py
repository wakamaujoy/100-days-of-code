class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        choice = input(f"q.{self.question_number}:{current_question.text}(TRUE/FALSE): ")


    def check_answer(self):
        current_ans = self.question_list

