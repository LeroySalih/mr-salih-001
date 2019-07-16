from datetime import datetime


class QuizDB:

  def __init__(self):
    self.attempts = {}
    self.history = [] 


  def makeKey(self, userId, moduleId, lessonId, activityId):
    return f"{userId}-{moduleId}-{lessonId}-{activityId}"

  def save_attempt(self, userId, moduleId, lessonId, activityId, score, answers):

    key = self.makeKey (userId, moduleId, lessonId, activityId)
    now = datetime.now()
    ts = datetime.timestamp(now)
    attempt =            {'userId': userId, 
                          'moduleId': moduleId,
                          'lessonId': lessonId,
                          'activityId': activityId,
                          'score': score,
                          'answers': answers, 
                          'timestamp': ts}
    
    self.attempts[key] = attempt
    self.history.append(attempt)
    

  def get_attempt(self, userId, moduleId, lessonId, activityId):
    key = makeKey(userId, moduleId, lessonId, activityId)
    return self.attempts.get(key, None)


quizDB = QuizDB()


    