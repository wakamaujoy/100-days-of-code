class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
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
        self.check_answer(choice, current_question.answer)
        self.final_score() 

    def check_answer(self, choice, correct_answer):
        if choice.lower() == correct_answer.lower():
            self.score += 1
            print(f"Correct, your points{self.score}/{self.question_number}")
        else:
            print("Wrong")

    def final_score(self):
        if self.question_number == len(self.question_list):
            print(f"You have completed the game, your total score is{self.score}/{self.question_number} ")




