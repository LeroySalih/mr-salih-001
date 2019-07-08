from itertools import groupby
from models.lo_models import LearningObjective
class LoDB:

  def init_data(self):

    self.learning_objectives = {
      'ind01*' : LearningObjective (
                    id='ind01*',
                    title="Computer Department expectations",
                    group='Induction',
                    developing="Can describe some of the 5B's and 5P's.",
                    satisfactory= "Can describe all of the 5B's and 5P's.",
                    exceeding= "Can identify behaviours that exemplify the 5B's and 5P's."
                    
      ),

      'ind02*' : LearningObjective (
                    id='ind01*',
                    title="Using the VLE",
                    group='Induction',
                    developing="Can access the VLE to download files and access messages.",
                    satisfactory= "Can submit homework to the VLE.",
                    exceeding= "Can describe the Rain Day process."
                    
      ),

      'ind03*' : LearningObjective (
                    id='ind03*',
                    title="Being a good Netizen",
                    group='Induction',
                    developing="Can expand and explain the ancronym THINK.",
                    satisfactory= "Can expand and explain the ancronym FAST.",
                    exceeding= "Can expand the ancronym THINK."
                    
      ),

      'oo01*' : LearningObjective (
                    id='oo01*',
                    title='Find relevant and accurate results from an online search engine',
                    group='Operating Online',
                    developing='Can produce a set of results from an online search engine.',
                    satisfactory= 'Can use advanced criteria in searching for results.',
                    exceeding= 'Can assess the quality and veracity of a result'
                    
      ),

      'oo02*' : LearningObjective (
                    id='oo02*',
                    title='Create, edit, save and upload documents in a cloud environment.',
                    group='Operating Online',
                    developing='Is able to create a document online.',
                    satisfactory= 'Is able to upload and edit a file created offline.',
                    exceeding= 'Is able to locate a file created online in the synchronised folder.'
                    
      ),
      
      'aict01': LearningObjective(
                    id='aict01',
                    title='Bring together different types of information to achieve a purpose',
                    group="Apply ICT",
                    developing='Can combine text information from a variety of sources.',
                    satisfactory= 'Can combine graphical information from a variety of sources.',
                    exceeding= 'Can multi media information (videos and audio) from a variety of sources.'
                    ),

      'aict02': LearningObjective(
                    id='aict02',
                    title='Produce information that is fit for purpose and audience, using accepted layouts and styles',
                    group='Apply ICT',
                    developing='Can produce work that partially meets a style guide.',
                    satisfactory= 'Can completely follow a style guide.',
                    exceeding= 'Can review the work of others and give feedback as to where a style guide is not followed.'
                    ),
      'ss01' : LearningObjective(
                    id='ss01',
                    title='Using the VLE.',
                    group='Software Skills',
                    developing='Requires assistance to use.',
                    satisfactory= 'Can confidently use.',
                    exceeding= 'Can troubleshoot other pupils issues.'
                  ),
      'ss02' : LearningObjective(
                    id='ss02',
                    title='Using a Word Processor.',
                    group='Software Skills',
                    developing='Requires assistance to use.',
                    satisfactory= 'Can confidently use.',
                    exceeding= 'Can troubleshoot other pupils issues.'
                  ),
       'ss03' :  LearningObjective(
                    id='ss03',
                    title='Using a Graphics Package.',
                    group='Software Skills',
                    developing='Requires assistance to use.',
                    satisfactory= 'Can confidently use.',
                    exceeding= 'Can troubleshoot other pupils issues.'
                  ),
      'hoc01' : LearningObjective(
                    id='hoc01',
                    title='I can remember and understand key historic figures from the world of computing.',
                    group='History of Computing',
                    developing='I can name all of the heroes of computing.',
                    satisfactory= 'I can analyse the impact of a hero of computing.',
                    exceeding= 'I can create the narrative of the hero of computing.'
                  ),
      'hoc02' : LearningObjective(
                    id='hoc02',
                    title='I can remember and understand key historic figures from the world of computing.',
                    group='History of Computing',
                    developing='I can name all of the heroes of computing.',
                    satisfactory= 'I can analyse the impact of a hero of computing.',
                    exceeding= 'I can create the narrative of the hero of computing.'
                  )
    }

  def __init__(self):
    self.init_data()

  def findById(id):
    return self.learning_objectives.get(id)

  def findByIds(self, *args):
    result = []

    for lo in self.learning_objectives.values():
    
      if lo.id in args:
        result.append(lo)
    
    return result
      
  def groupByType(self, los):
    """ return the Learning Objectives as a grouped iterable """
    
    # sort all lo's by group
    data = sorted(los, key=lambda x: x.group)

    #group the LO's by group
    groups = groupby(data, lambda x: x.group)

    log_data = []

    for group in groups:
      print (group)
      log_data_item = [group, list(group[1])]
      log_data.append(log_data_item)

    return log_data;
    

loDB = LoDB()
  