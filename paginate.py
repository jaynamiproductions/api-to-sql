import sqlite3
import requests
import pandas as pd

def paginate_tosql(url, db_name):
    conn = sqlite3.connect(db_name)
    limit = 1500
    offset = 0
    if url.endswith('json'):
        while True:
            base = url
            api = base + '?$limit='+ str(limit) +'&$offset='+str(offset) +'&$order=:id'
            resp = requests.get(api).json()
            df = pd.DataFrame(resp)
            df = df.applymap(str)
            df.to_sql('providers',conn,if_exists='append',index=False)
            if df.shape[0] != limit:
                break
            offset += 1000
    else:
        while True:
            base = url
            api = base + '?size='+ str(limit) +'&offset='+str(offset)
            resp = requests.get(api).json()
            df = pd.DataFrame(resp)
            df = df.applymap(str)
            df.to_sql('table_name',conn,if_exists='append',index=False)
            if df.shape[0] != limit:
                break
            offset += 1500    

# TEST URLs 
# (open-source Socrata dataset from CDC, 240k rows)
# paginate_tosql('https://data.cdc.gov/resource/bugr-bbfr.json','database.db')

# (open-source dataset from CMS, 1.8m rows)
# paginate_tosql('https://data.cms.gov/data-api/v1/dataset/c99b5865-1119-4436-bb80-c5af2773ea1f/data','new.db')
