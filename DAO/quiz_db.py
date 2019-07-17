from datetime import datetime
from flask import current_app as app 

class QuizDB:

  def __init__(self):
    self.answers = {}
    self.history = [] 


  def makeKey(self, userId, moduleId, lessonId, activityId):
    return f"{userId}-{moduleId}-{lessonId}-{activityId}"

  def saveActivityAnswers(self, userId, moduleId, lessonId, activityId, score, answers):
    app.logger.debug(f'{userId} {answers}')
    key = self.makeKey (userId, moduleId, lessonId, activityId)
    now = datetime.now()
    ts = datetime.timestamp(now)
    attempt =            {'userId': userId, 
                          'moduleId': moduleId,
                          'lessonId': lessonId,
                          'activityId': int(activityId),
                          'score': score,
                          'answers': answers, 
                          'timestamp': ts}
    
    self.answers[key] = attempt
    self.history.append(attempt)
    

  def getAnswersForLesson(self, userId, moduleId, lessonId):
    result = {}
    attempts = list(filter(lambda item: item['userId'] == userId and 
                                   item['moduleId'] == moduleId and 
                                   item['lessonId'] == lessonId, 
                                   self.answers.values())
                    )
   

    
      
    for attempt in attempts:
      result[int(attempt['activityId'])] = attempt 

    return result


quizDB = QuizDB()


    