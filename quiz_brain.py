class QuizBrain(object):
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        response = input(f"Q{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(response, current_question.answer)

    def still_has_questions(self):
        num_of_questions = len(self.question_list)
        if num_of_questions == self.question_number:
            decision = False
        else:
            decision = True
        return decision

    def check_answer(self, user_response, correct_answer):

        if user_response.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your score is: {self.score}/{self.question_number}")
        print()