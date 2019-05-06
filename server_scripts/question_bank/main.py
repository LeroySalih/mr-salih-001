import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import pymysql.cursors
import sys 

drop_tables_sql = """
DROP TABLE IF EXISTS QUESTIONS; DROP TABLE IF EXISTS QUIZZES"""


create_table_questions_sql = """
CREATE TABLE QUESTIONS (
	question_id				INT 	AUTO_INCREMENT PRIMARY KEY,
  user_id           varchar(255),
	created					  date	NOT NULL,
	subject					  varchar(255) NOT NULL,
	question_img			varchar(255) ,
	question_text     varchar(255) ,
	answer_1_img			varchar(255) ,
	answer_1_text			varchar(255) ,
	answer_2_img			varchar(255) ,
	answer_2_text			varchar(255) ,
	answer_3_img			varchar(255) ,
	answer_3_text			varchar(255) ,
	answer_4_img			varchar(255) ,
	answer_4_text			varchar(255) ,
	correct_answer			char(1)
);
""" 

create_table_quizzes_sql = """ 
CREATE TABLE QUIZ_QUESTIONS (
	quiz_id				    INT			NOT NULL,
	question_number		INT			NOT NULL,
	question_id			  INT			NOT NULL	
);
"""

create_table_answers_sql = """ 
CREATE TABLE ANSWERS (
	answer_id			INT			AUTO_INCREMENT PRIMARY KEY,
	quiz_id				INT			NOT NULL,
	user_id				INT			NOT NULL,
	answer_selected		char(1)		NOT NULL,
	is_correct			INT			NOT NULL
);
"""




delete_sql = """
DELETE QUESTIONS WHERE author_id={author} and subject="{subject}"
"""

insert_sql = """INSERT INTO QUESTIONS (
  user_id             ,
	created					   ,
	subject					   ,
	question_img			 ,
	question_text      ,
	answer_1_img		   ,
	answer_1_text			 ,
	answer_2_img			 ,
	answer_2_text			 ,
	answer_3_img			 ,
	answer_3_text			 ,
	answer_4_img			 ,
	answer_4_text			 ,
	correct_answer		
)
VALUES (
  "{user_id}",
  "{created}",
  "{subject}",
  "{question_img}",
  "{question_text}",
  "{answer_1_img}",
  "{answer_1_text}",
  "{answer_2_img}",
  "{answer_2_text}",
  "{answer_3_img}",
  "{answer_3_text}",
  "{answer_4_img}",
  "{answer_4_text}",
  "{correct_answer}"
)
"""






def create_tables(db, cursor):
  
  try:

    tables = ['QUESTIONS', 'QUIZZES', 'ANSWERS']
    for table in tables:
      cursor.execute("DROP TABLE IF EXISTS {}".format(table))

    cursor.execute(create_table_questions_sql)
    cursor.execute(create_table_quizzes_sql)
    cursor.execute(create_table_answers_sql)
    db.commit()
    return True
  except error as Exception:
   # print (error)
    db.rollback()
    return False
  
  
  
  #cursor.execute(create_tables_sql)

def add_questions(db, cursor, df):
  
  try:
    #cursor.execute(delete_sql.format(row[1]['Author']))
    for row in df.iterrows():
      cursor.execute(insert_sql.format(
        user_id=row[1]['Author'],
        created=row[1]['Date'],
        subject=row[1]['Subject'],
        question_img=row[1]['Question Image'],
        question_text=row[1]['Question Text'],
        answer_1_img=row[1]["Answer 1 Img"],
        answer_1_text=row[1]["Answer 1 Text"],
        answer_2_img=row[1]["Answer 2 Img"],
        answer_2_text=row[1]["Answer 2 Text"],
        answer_3_img=row[1]["Answer 3 Img"],
        answer_3_text=row[1]["Answer 3 Text"],
        answer_4_img=row[1]["Answer 4 Img"],
        answer_4_text=row[1]["Answer 4 Text"],
        correct_answer=row[1]["Correct Answer"]
      ))
    db.commit()
    return True
  except error as Exception:
    db.rollback()
    #print(error)
    return False







if (__name__ == "__main__"):

  
  db = pymysql.connect(host='u28rhuskh0x5paau.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                             user='f85i420whipnx6fk',
                             password='mp57xmd4bu6bf4cj',
                             db='i9k89ae7frjnnm63',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

  cursor = db.cursor()


  if ("-c" in sys.argv):
    print("Creating Tables")
    if create_tables(db, cursor):
      print ("OK")
    else:
      print ("An error occurred")

  if ("-add" in sys.argv):
    file_name = sys.argv[len(sys.argv) - 1]
    print ("Adding questions from {}".format(file_name))
    df = pd.read_excel('salih.xlsx', sheet_name='Sheet1')
    if add_questions(db, cursor, df):
      print ("OK")
    else:
      print("An error occurred")

  print ("Done")
  db.close()