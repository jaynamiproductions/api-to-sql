import sqlite3
import requests
import pandas as pd

def paginate_tosql(url, db_name):
    conn = sqlite3.connect(db_name)
    limit = 1000
    offset = 0
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

# TEST URL (open-source Socrata dataset from CDC)
paginate_tosql('https://data.cdc.gov/resource/bugr-bbfr.json','database.db')
