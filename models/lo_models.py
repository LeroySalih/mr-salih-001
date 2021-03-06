from itertools import groupby
import uuid 

class Module:

  def __init__(self,  id, title, description, url):

    self.id = id
    self.title = title
    self.description = description 
    self.url = url
    self.lessons = {}
  


  @property 
  def path(self):
    return self.id 

  def add_lesson(self, lesson, replace=False):

    """ 
    Add a lesson to the lesson dictionary.
    Will overwrite a lesson with the same id.

    returns self to allow chaining
    """

    if self.lessons.get(lesson.id) != None and not replace:
      raise NameError(f'WARNING: Overwriting lesson id {lesson.id}')

    self.lessons[lesson.id] = lesson
    return self.lessons[lesson.id] 





class Lesson:

  def __init__ (self, id, number, title, description, hw_due, hw_set):
    self.id = id
    self.number = number
    self.title = title 
    self.description = description 
    self.hw_due = hw_due 
    self.hw_set = hw_set 
    self.resources = []
    self.activities = []
    self.los = []
    self.module = {'id': 'Not Set'}

  @property  
  def timeline(self):
   
    return sorted(self._timeline.values(), key=lambda x: x.time, reverse=False)

  def addActivities(self, *activities):
    
    for activity in activities:
      self.activities.append(activity)
      

  def setLearningObjectiveIds(self, *args):
    """ adds the id of the lo to the list of los.
        will replace existing lo's with the same id
        returns self to allow chaining
    """
    self.los = args

    return self 



class LearningObjective : 

  def __init__(self, id, title, group, developing, satisfactory, exceeding):
    self.id = id
    self.title = title
    self.group = group 
    self.developing = developing
    self.satisfactory = satisfactory 
    self.exceeding = exceeding


  def __repr__(self):
    return f'<LearningObjective id:{self.id} title:{self.title}>'

