from models.lo_models import LearningObjective, Lesson
from models.lo_models import Module
from models.activity import Activity, VideoActivity, QuizActivity, RateProgressActivity, RecapActivity, LoPuActivity
from models.quiz import Quiz

from DAO.lo_db import loDB

class ModuleDB:

  def create_history_of_computing(self):
    module = Module(
            'history-of-computing', 
            'History of Computing', 
            'In this module, pupils will learn how computers have changed from simple mechanical devices to the sophisticated machines we see today.',
            'history-of-computing'
            )

    lesson1 = Lesson('introduction-to-the-history-of-computing',1, 'Introduction to the History of Computing','In this lesson, pupils will be introduced to the project, the generations of computing and the historical figures.', 'None', 'None')
    lesson1.setLearningObjectiveIds( 'hoc01', 'hoc02')
    module.add_lesson(lesson1)

    lesson2 = Lesson('styling-my-work',2, 'Styling my Work','In this lesson, pupils will practice applying styles and layouts to ensure that documents are consistent and easy to read.', 'None', 'None')
    lesson2.setLearningObjectiveIds( 'aict02', 'ss02')
    module.add_lesson(lesson2)

    lesson3 = Lesson('searching-online',3, 'Searching Online','In this lesson, pupils will practice searching for information online.  They will also discuss how to evaluate their results.', 'None', 'None')
    lesson3.setLearningObjectiveIds( 'oo01*')
    module.add_lesson(lesson3)

    lesson4 = Lesson('project',4, 'Project','In this lesson, pupils will complete their project work and offer feedback to each other.', 'None', 'None')
   #lesson4.setLearningObjectiveIds( 'oo01*')
    module.add_lesson(lesson4)

    self.modules[module.id] = module 

  def create_induction(self):
    module = Module(
      'induction', 
      'Induction', 
      'In this module, pupils will learn the rules and expectations of the Computing Department.  They will gain an overview of the modules that will be covered, the safety and school closure procedures that must be followed, and how to use key software applications.',
      'induction')
 
    lesson1 = Lesson('computing-department-expectations',1, 'Computing Department Expectations',"In this lesson, pupils will be introduced to the Computing Department and will be introduced the the 5B's and 5P's of the computer department expectations. ", 'None', 'None')
    lesson1.setLearningObjectiveIds( 'ind01*')
    module.add_lesson(lesson1)

    lesson2 = Lesson('using-the-vle',1, 'Using the VLE',"In this lesson, pupils will be introduced to the VLE and how to use the software. ", 'None', 'None')
    lesson2.setLearningObjectiveIds( 'ind02*')
    module.add_lesson(lesson2)

    lesson3 = Lesson('netizens',1, 'Netizens',"In this lesson, pupils will be introduced to the importance of being a good Netizen. ", 'None', 'None')
    lesson3.setLearningObjectiveIds( 'ind03*')
    module.add_lesson(lesson3)

    self.modules[module.id] = module 

  def create_office_online(self):
    module = Module(
      'onedrive-and-office-online', 
      'One Drive & Office Online', 
      'In this introduction to OneDrive and Office Online, pupils will learn to create, edit, save and upload documents in the cloud so that they can <b>create and edit documents from school or home</b>.',
      'one-drive-office-online')

    lesson1 = Lesson(
      'onedrive-and-office-online',
      1, 
      'OneDrive & Office online',
      'How to create, edit, save, upload and access documents using OneDrive and Office Online', 
      'None', 
      'None')
    lesson1.setLearningObjectiveIds( 'ss02', 'oo02*')
    lesson1.starter = """
      <ul>
        <li>Work in groups of 2's or 3's</li>
        <li>Take one piece of paper per group.</li>
        <li>Discuss and identify 3 difficulties of <b>using thumb drives</b></li>
      </ul>"""
    lesson1.resources = [{'url': '', 'text':'Lesson Slides'}, 
                         {'url': '', 'text':'Cheat Sheet'}, 
                        ]

    q1 = Quiz('q1', 'Using OneDrive?' )
    q1.add_question(0, 'What is OneDrive?', ['A house with one drive', 'A software service that can store files.'],[False, True])
    q1.add_question(1, 'Which software company creates OneDrive?', ['Microsoft', 'BISAK', 'Google', 'DropBox'],[True, False, False, False])

    q2 = Quiz('q2', 'Uploading Files.' )
    q2.add_question(0, 'Test Question 1?', ['Answer 1', 'Answer 2.'],[False, True])
    q2.add_question(1, 'Test Question 2?', ['Answer 1', 'Answer 2.'],[True, False])


    lesson1.addActivities(
          Activity(10, 'Starter', """
          <h2>In pairs, create a list of the issues you may face when you use a thumbdrive to transport files to and from home.</h2> 
          """), 
          VideoActivity(10,  'What is OneDrive?', 'https://www.dropbox.com/s/tkjpefa581rsibg/Internet%20Safety%20-%20Newsround%20Caught%20In%20The%20Web%20%289%20Feb%202010%29.mp4?raw=1'),
          QuizActivity(10, 'What is OneDrive?', q1),
          Activity(15, 'Uploading and locating files in the Cloud.', content=""),
          QuizActivity(10, 'Test Quiz?', q2),
          Activity(0, '(Extension) What is OneDrive Version History?', content=""), 
          RateProgressActivity(5, 'Rate your progress'),
          RecapActivity(10, 'Recap'),
          LoPuActivity(5, 'LoPu')
          #,
          # QuizItem    ('00:45',  f"CFU: {tlQuiz.title}", tlQuiz),
          
     #     TimelineItem('00:50',  BringItAllTogetherItem('Bring It All Together'),
     #     TimelineItem('00:54',  RateYourProgressItem('Rate Your Progress'),
     #     TimelineItem('00:57',  NailItDown('Nail It Down'),
     #     TimelineItem('00:59',  LOPU()),
          )    

    

    lesson1.homework = """From `vle"""
    
    
    module.add_lesson(lesson1)

    self.modules[module.id] = module

  
  def init_data(self):
    self.create_history_of_computing()
    self.create_induction()
    self.create_office_online()
    
  def __init__(self):
    self.modules = {}
    self.init_data()
  
  def findById(self, moduleId):
    """
      return: Module with matching moduleId
    """
    return self.modules.get(moduleId)

  def findByUrl(self, url):
    """
      return: Module with matching the Url
    """
    #result = self.modules.values().filter(lambda m: m.url == url)
    results = list(filter(lambda m: m.url == url, self.modules.values()))
    
    if len(results) == 0:
      return None 
    else:
      return results[0]


  def getAllLOIds(self, moduleId):
    """ loop through all lessons, compile a list of LO id's """

    module = self.findById(moduleId)
  
    result = []
    for lesson in module.lessons.values():
      result = result + list(lesson.los)
        
    return result;

  def populateLessons(self, module):
    #get all lo's for the module
    #get the LO's by ids
    #assign each LO tby id 
    ids = self.getAllLOIds(module.id)
    
    for lesson in module.lessons.values():
      lesson.learning_objectives = {}
      for loId in lesson.los:
        lo = loDB.learning_objectives.get(loId)
        if (lo != None):
          lesson.learning_objectives[lo.id] = lo 
        
    
  def findLessonByIds (self, moduleId, lessonId):
    module = self.modules.get(moduleId)
    if module != None:
      return module.lessons.get(lessonId)
    else: 

      
      raise NameError(f'No module found with matching id {moduleId}')
      return None 
    
  
moduleDB = ModuleDB()



  


"""
    loGroup1 = LearningObjectiveGroup('applying_ict', 'Applying ICT')
    loGroup1.add_lo(LearningObjective(
      id='aict01',
      title='Bring together different types of information to achieve a purpose',
      developing='Can source information from a variety of online and offline sources',
      satisfactory= 'Can correctly reference sources',
      exceeding= 'Can assess the quality and veracity of online sources')
      )

    loGroup1.add_lo(LearningObjective(
      id='aict02',
      title='Produce information that is fit for purpose and audience, using accepted layouts and styles',
      developing='Can produce work that partially meets a style guide.',
      satisfactory= 'Can completely follow a style guide.',
      exceeding= 'Can review the work of others and give feedback as to where a style guide is not followed.')
      )


    loGroup2 = LearningObjectiveGroup('software', 'Software Skills')
    loGroup2.add_lo(LearningObjective(
      id='ss01',
      title='Using the VLE.',
      developing='Requires assistance to use.',
      satisfactory= 'Can confidently use.',
      exceeding= 'Can troubleshoot other pupils issues.')
    )
    
    loGroup2.add_lo(LearningObjective(
      id='ss02',
      title='Using a Word Processor.',
      developing='Requires assistance to use.',
      satisfactory= 'Can confidently use.',
      exceeding= 'Can troubleshoot other pupils issues.')
    )

    loGroup2.add_lo(LearningObjective(
      id='ss03',
      title='Using a Graphics Package.',
      developing='Requires assistance to use.',
      satisfactory= 'Can confidently use.',
      exceeding= 'Can troubleshoot other pupils issues.')
    )

    loGroup3 = LearningObjectiveGroup('heroes-of-computing', 'Heroes Of Computing')
    
    loGroup3.add_lo(LearningObjective(
      id='hoc1',
      title='I can remember and understand the generations of computing.',
      developing='I can list some of the generations of computing.',
      satisfactory= 'I can list all of the generations of computing.',
      exceeding= 'I can list all generations and provide examples of the generations of computing.')
    )
    
    loGroup3.add_lo(LearningObjective(
      id='hoc2',
      title='I can remember and understand key historic figures from the world of computing.',
      developing='I can name all of the heroes of computing.',
      satisfactory= 'I can analyse the impact of a hero of computing.',
      exceeding= 'I can create the narrative of the hero of computing.')
    )

"""
    


