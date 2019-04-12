sqlDROP_USER_TABLE = """
DROP TABLE IF EXISTS users;
"""

sqlCREATE_USER_TABLE = """
CREATE TABLE users (
  id    INT   AUTO_INCREMENT  PRIMARY KEY,
  first_name  VARCHAR(255)
);
"""

sqlADD_USERS = """
INSERT INTO users (first_name) VALUES ('admin');
"""

sqlREAD_USERS = """
SELECT * FROM  users;
"""