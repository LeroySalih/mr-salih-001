

from models.classes import Class 
from models.user import User

class ClassDB:

  def __init__(self):
    self.__classes = {}
    self.__users = {}
    self.init_users()
    self.init_classes()
    

  def addClass(self, _class, replace=False):
    
    if not replace and self.__classes.get(_class.id) != None:
      raise NameError ('Class Id already exists')

    self.__classes[_class.id] = _class 
    
  def init_users(self):

    self.__users = {
      1 : User({'id': 1, 'username': 'teacher1', 'password': 'password123', 'is_teacher': True}),
      11 : User({'id': 11, 'username': 'pupil1', 'password': 'password123', 'is_teacher': False}),
      12 : User({'id': 12, 'username': 'pupil2', 'password': 'password123', 'is_teacher': False}),
      13 : User({'id': 13, 'username': 'pupil3', 'password': 'password123', 'is_teacher': False}),
    }

  def init_classes(self):

    class1 = Class(13,'7C-COMP', 'Year 7C Computing Class', 1)
    class1.add_pupilIds(11,12,13)
    self.addClass(class1)

    class2 = Class(11,'7A-COMP', 'Year 7A Computing Class', 1)
    class2.add_pupilIds(11,12,13)
    self.addClass(class2)

    class3 = Class(12,'7B-COMP', 'Year 7B Computing Class', 1)
    class3.add_pupilIds(11,12,13)
    self.addClass(class3)



  @property
  def classes (self):
    return sorted(self.__classes.values(), key=lambda c: c.title)


classDB = ClassDB()
     