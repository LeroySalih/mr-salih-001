class Activity:
  
  def __init__(self, duration, title, content):
    self.duration = duration 
    self.title = title 
    self.content = content
    

class VideoActivity (Activity):

  def __init__(self, duration, title, url):
    super().__init__(duration, title, content="") 
    self.url = url 


class QuizActivity (Activity):

  def __init__(self, duration, title, quiz):
    super().__init__(duration, title, content="") 
    self.quiz = quiz 


class RateProgressActivity (Activity):
  
  def __init__(self, duration, title):
    super().__init__(duration, title, content="") 
    
class RecapActivity (Activity):
  
  def __init__(self, duration, title):
    super().__init__(duration, title, content="") 
    
class LoPuActivity (Activity):
  
  def __init__(self, duration, title):
    super().__init__(duration, title, content="") 
     


#Add other Twinkle Subject Planary Slides
"""
class RateYourProgressItem:
  def __init__(self, time, title):
    super().__init__(time, title)

class BringItAllTogetherItem:
  def __init__(self, text):
    super().__init__(time, title)
    
class NailItDownItem:
  def __init__(self, text):
    super().__init__(time, title)  
"""




