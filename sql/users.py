sqlDROP_USER_TABLE = """
DROP TABLE IF EXISTS users;
"""

sqlCREATE_USER_TABLE = """
CREATE TABLE users (
  id            INT AUTO_INCREMENT  PRIMARY KEY,
  username      VARCHAR(255) NOT NULL,
  password      VARCHAR(1024) NOT NULL,
  first_name    VARCHAR(255)
);
"""

sqlADD_USERS = """
INSERT INTO users ( username, password, first_name) VALUES ( '{username}', '{password}', '{first_name}');
"""

sqlREAD_USERS = """
SELECT * FROM  users;
"""

sqlREAD_USER = """
SELECT * FROM users WHERE id={};
"""

sqlREAD_USER_BY_FIRST_NAME = """
SELECT * FROM users WHERE first_name='{}'
"""

sqlREAD_USER_BY_USERNAME = """
SELECT * FROM users WHERE username='{}';
"""

