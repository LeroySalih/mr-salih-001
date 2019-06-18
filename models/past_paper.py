from flask import Flask, current_app


from werkzeug.security import generate_password_hash, check_password_hash

from sql.db import get_db
from sql.past_papers import sqlDROP_PAST_PAPER_TABLE, sqlCREATE_PAST_PAPER_TABLE, sqlREAD_PAST_PAPERS, sqlREAD_PAST_PAPER_LAST_ADDED, sqlADD_PAST_PAPER




class PastPaperException (Exception):

  def __init__(self, expression, message):
        self.expression = expression
        self.message = message


#[START model]
class PastPaper():
  
  __id = 0
  __level = "not set"
  __year = "not set"
  __month = "not set"
  __title = "not set"
  __paper_link = "not set"
  __ms_link = "not set"
  __sols_link = "not set"


  def __init__(self, dict):

    if (dict == None):
      raise PastPaperException(dict, "Dictionary is None.  This is not allowed when creating a Past Paper object.")

    #Constructor
    for key in dict:
      setattr(self, key, dict[key])

  def __repr__(self):
    return f"""<PastPaper (id={self.__id}, 
              level='{self.__level}', 
              year='{self.__year}', 
              month='{self.__month}'
              title='{self.__title}'
              paper_link='{self.__paper_link}'
              ms_link='{self.__ms_link}'
              sols_link='{self.__sols_link}'
              )>"""


  def to_dict(self):
    return {'id': self.id, 
            'level': self.__level, 
            'year': self.__year, 
            'month': self.__month,
            'title': self.__title, 
            'paper_link': self.__paper_link, 
            'ms_link': self.__ms_link,
            'sols_link':self.__sols_link
            }
  

  @property
  def id(self):
    return self.__id
  
  @id.setter
  def id(self, val):
    self.__id = val

  @property
  def level(self):
    return self.__level

  @level.setter
  def level(self, val):
    self.__level = val


  @property
  def year(self):
    return self.__year

  @year.setter
  def year(self, val):
    self.__year = val

  @property
  def month(self):
    return self.__month

  @month.setter
  def month(self, val):
    self.__month = val

  @property
  def title(self):
    return self.__title

  @title.setter
  def title(self, val):
    self.__title = val
  
  @property
  def paper_link(self):
    return self.__paper_link

  @month.setter
  def paper_link(self, val):
    self.__paper_link = val

  @property
  def ms_link(self):
    return self.__ms_link

  @ms_link.setter
  def ms_link(self, val):
    self.__ms_link = val

  @property
  def sols_link(self):
    return self.__sols_link

  @sols_link.setter
  def sols_link(self, val):
    self.__sols_link = val


  @staticmethod
  def get_all():
      
      db = None 
      users = []

      try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute(sqlREAD_USERS)

        results = cursor.fetchall()

        for record in results:
          users.append(User(record))

      except pymysql.err.OperationalError as e:
        current_app.logging.error("The db threw an exception")

      finally:
        if db != None:
          db.close()

        return users

      

  @staticmethod
  def get_by_id(id): 
    db = get_db()
    cursor = db.cursor()
    cursor.execute(sqlREAD_USER.format(id))
    result = cursor.fetchone()
    db.close()
    if result == None: 
      return None
    return User(result) 

  @staticmethod 
  def get_by_first_name(first_name):
    users = []
    db = get_db()
    cursor = db.cursor()
    cursor.execute(sqlREAD_USER_BY_FIRST_NAME.format(first_name))
    for record in cursor.fetchall():
      users.append(User(record))
    db.close()
    return users

  @staticmethod
  def get_by_username(username):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(sqlREAD_USER_BY_USERNAME.format(username))
    user = cursor.fetchone()
    db.close()
    if user == None:
      return None 
    else: 
      return User(user)

  @staticmethod
  def get_last_added():
    db = get_db()
    cursor = db.cursor()
    cursor.execute(sqlREAD_PAST_PAPER_LAST_ADDED)
    pp = cursor.fetchone()
    db.close()

    if pp == None:
      return None
    else:
      return PastPaper(pp)


  @staticmethod
  def add_past_paper(u):
    db = get_db()
    cursor = db.cursor()
    cmdSQL = sqlADD_PAST_PAPER.format(level=u.level, 
    year=u.year, 
    month=u.month,
    title=u.title,
    paper_link=u.paper_link,
    ms_link=u.ms_link,
    sols_link=u.sols_link
    )

    cursor.execute(cmdSQL)

    db.commit()
    cursor.execute(sqlREAD_PAST_PAPER_LAST_ADDED)
    #reload user with ID
    pp_data = cursor.fetchone()
    db.close()
    return PastPaper(pp_data)
    
  
  @staticmethod
  def create_tables():
    db = get_db()
    cursor = db.cursor()
    cursor.execute(sqlDROP_PAST_PAPER_TABLE)
    cursor.execute(sqlCREATE_PAST_PAPER_TABLE)
    db.close()


  @staticmethod
  def test_add_past_paper():
    pp_data = {'id':1, 
      'level': 'Level 4-6', 
      'year':'2019', 
      'month': 'Jan', 
      'title':'Paper 1H',
      'paper_link':'Paper Here',
      'ms_link':'MS Here',
      'sols_link':'Sols Here',
      }
    pp = PastPaper.add_past_paper(PastPaper(pp_data))
    print (pp)

    


#[END model]


if __name__=="__main__":
  pp_data = {'id':1, 
      'level': 'Level 4-6', 
      'year':'2019', 
      'month': 'Jan', 
      'title':'Paper 1H',
      'paper_link':'Paper Here',
      'ms_link':'MS Here',
      'sols_link':'Sols Here',
      }

  pp = PastPaper(pp_data)

  print (pp)


  

  



  #


