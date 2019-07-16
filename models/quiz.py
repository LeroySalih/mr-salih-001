class Quiz:

  def __init__(self, id, title):
    self.id = id
    self.title = title
    self.questions = {} 

  def add_question (self, number, text, answers, correct):
    self.questions[number] = {'text': text, 'answers': answers, 'correct': correct }

  def check_answers(self, answers):
    keys = answers.keys()
    correct = 0
    for key in keys:
      user_answers = answers[key]
      correct_answers = self.questions[int(key)]['correct'] 

      if user_answers == correct_answers:
        correct = correct  + 1

    return  correct


