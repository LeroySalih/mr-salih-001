sqlDROP_PAST_PAPER_TABLE = """
DROP TABLE IF EXISTS past_papers;
"""

sqlCREATE_PAST_PAPER_TABLE = """
CREATE TABLE past_papers (
  id            INT AUTO_INCREMENT  PRIMARY KEY,
  level         VARCHAR(255) NOT NULL,
  year          VARCHAR(255) NOT NULL,
  month         VARCHAR(255) NOT NULL,
  title         VARCHAR(255) NOT NULL,
  paper_link    VARCHAR(255),
  ms_link       VARCHAR(255),
  sols_link     VARCHAR(255) 
);
"""


sqlADD_PAST_PAPER = """
INSERT INTO past_papers ( level, year, month, title, paper_link, ms_link, sols_link) VALUES ( '{level}', '{year}', '{month}', '{title}', '{paper_link}', '{ms_link}', '{sols_link}');
"""

sqlREAD_PAST_PAPERS = """
SELECT * FROM  past_papers ORDER BY level, year, month, title;
"""

sqlREAD_PAST_PAPER_LAST_ADDED = """
select  * from past_papers where id = LAST_INSERT_ID();
"""

sqlREAD_PAST_PAPER_BY_ID = """
SELECT * FROM users WHERE id={};
"""

sqlREAD_PAST_PAPER_BY_LEVEL = """
SELECT * FROM past_papers WHERE level='{}' ORDER BY level, year, month, title
"""



