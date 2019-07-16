class Class:

  def __init__(self,id, title, description, teacherId):

    self.id = id
    self.title = title 
    self.description = description 
    self.teacherId = teacherId 
    self.pupilIds = []

  def add_pupilIds(self, *pupilIds):
    for pupilId in pupilIds:
      self.pupilIds.append(pupilId)

   