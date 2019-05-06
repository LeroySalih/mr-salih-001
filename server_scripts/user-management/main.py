import pymysql
import warnings 
import pymysql.cursors

import db

if __name__ == "__main__":
  print("Testing")

  cursor = db.cursor
  cursor.execute("SELECT VERSION()")
  data = cursor.fetchone()
  print(data)