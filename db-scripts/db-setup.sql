USE MRSALIH001;

DROP TABLE IF EXISTS USERS;

CREATE TABLE USERS (
  user_id         INT(11) NOT NULL AUTO_INCREMENT,
  user_name       varchar(255) NOT NULL,
  first_name      varchar(255) NOT NULL,
  pwd             varchar(255) NOT NULL,
  CONSTRAINT pk_user_id PRIMARY KEY (user_id)
);

INSERT INTO USERS (user_name, first_name, pwd) VALUES ('test1', 'test 1', 'test1');
INSERT INTO USERS (user_name, first_name, pwd) VALUES ('test2', 'test 2', 'test2');
INSERT INTO USERS (user_name, first_name, pwd) VALUES ('test3', 'test 3', 'test3');

SELECT * FROM USERS;
