import sqlite3
import requests
import pandas as pd

def paginate_tosql(url):
    conn = sqlite3.connect('database.db')
    limit = 1000
    offset = 0
    while True:
        url += '?$limit='+ str(limit) +'&$offset='+str(offset)+'&$order=:id'
        resp = requests.get(url).json()
        df = pd.DataFrame(resp)
        df = df.applymap(str)
        df.to_sql('table',conn,if_exists='append',index=False)
        if df.shape[0] != limit:
            break
        offset += 1000
    return pd.read_sql('SELECT * FROM table',conn)

