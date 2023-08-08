import sqlite3
import requests
import pandas as pd

def paginate_tosql(url, db_name):
    conn = sqlite3.connect(db_name)
    limit = 1000
    offset = 0
    if url.endswith('json'):
        while True:
            base = url
            api = base + '?$limit='+ str(limit) +'&$offset='+str(offset)+'&$order=:id'
            resp = requests.get(api).json()
            df = pd.DataFrame(resp)
            df = df.applymap(str)
            df.to_sql('providers',conn,if_exists='append',index=False)
            if df.shape[0] != limit:
                break
            offset += 1000
    elif url.endswith('data'):
        while True:
            base = url
            api = base + '?size='+ str(limit) +'&offset='+str(offset)
            resp = requests.get(api).json()
            df = pd.DataFrame(resp)
            df = df.applymap(str)
            df.to_sql('providers',conn,if_exists='append',index=False)
            if df.shape[0] != limit:
                break
            offset += 1000
# TEST URLs (open-source APIs from CMS and CDC)
# paginate_tosql('https://data.cms.gov/data-api/v1/dataset/f1a8c197-b53d-4c24-9770-aea5d5a97dfb/data','new.db')
# paginate_tosql('https://data.cdc.gov/resource/bugr-bbfr.json','database.db')
