# import pandas as pd
# import pandas_gbq
# from google.oauth2 import service_account
from unittest import result
from google.cloud import bigquery


cred = "/Users/thetpaing/Documents/Backup/IP/bigquery-test-350706-f94ca5b2fbed.json"
client = bigquery.Client(project="bigquery-test-350706",credentials=cred,location="us-central1")
sql = "select * from bigquery-test-350706.burma_rice.selected_data"
result = client.query(sql)
# df = pd.read_gbq(sql, project_id="bigquery-test-350706", credentials=cred)

for row in result:
    title = row['title']