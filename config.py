import os

from creds import CLOUDSQL_USER, CLOUDSQL_PASSWORD, CLOUDSQL_DATABASE






DATA_BACKEND = 'datastore'
PROJECT_ID = 'flask003'

CLOUD_CONNECTION_NAME = 'flask003:europe-west6:mrsalih-com'

# To start the proxy server:
# /Users/leroy/cloud_sql_proxy -instances="flask003:europe-west6:mrsalih-com"=tcp:3306

LOCAL_SQLALCHEMY_DATABASE_URI = ('mysql+pymysql://{user}:{password}@127.0.0.1:3306/{database}').format(
  user=CLOUDSQL_USER,
  password=CLOUDSQL_PASSWORD,
  database=CLOUDSQL_DATABASE)


LIVE_SQLALCHEMY_DATABASE_URI =  (
  'mysql+pymysql://{user}:{password}@localhost/{database}'
  '?unix_socket=/cloudsql/{connection_name}').format(
    user=CLOUDSQL_USER, 
    password=CLOUDSQL_PASSWORD,
    database=CLOUDSQL_DATABASE,
    connection_name=CLOUD_CONNECTION_NAME)


if os.environ.get('GAE_INSTANCE'):
  SQLALCHEMY_DATABASE_URI = LIVE_SQLALCHEMY_DATABASE_URI
else:
  SQLALCHEMY_DATABASE_URI = LOCAL_SQLALCHEMY_DATABASE_URI
