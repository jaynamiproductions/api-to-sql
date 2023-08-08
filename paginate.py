import sqlite3
import requests
import pandas as pd

def paginate_tosql(url):
    conn = sqlite3.connect('database.db')
    limit = 1000
    offset = 0
    while True:
        base = url
        api = base + '?$limit='+ str(limit) +'&$offset='+str(offset)+'&$order=:id'
        resp = requests.get(api).json()
        df = pd.DataFrame(resp)
        df = df.applymap(str)
        df.to_sql('table',conn,if_exists='append',index=False)
        if df.shape[0] != limit:
            break
        offset += 1000
