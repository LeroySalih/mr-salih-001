import os

from creds import CLOUDSQL_USER, CLOUDSQL_PASSWORD, CLOUDSQL_DATABASE


DATA_BACKEND = 'datastore'
PROJECT_ID = 'flask003'

#CLOUD_CONNECTION_NAME = 'flask003:europe-west6:mrsalih-com'
CLOUD_CONNECTION_NAME = 'flask003:us-central1:mr-salih-001'

# To start the proxy server:
# /Users/leroy/cloud_sql_proxy -instances="flask003:europe-west6:mrsalih-com"=tcp:3306
# /Users/leroy/cloud_sql_proxy -instances="flask003:us-central1:mr-salih-001"=tcp:3306



