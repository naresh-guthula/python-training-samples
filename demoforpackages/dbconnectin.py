import pyodbc

conn = pyodbc.connect('DRIVER={SQL Server};server=DESKTOP-F91KEVI\SA1')
cur = conn.cursor()

query = 'select @@version'

print(cur.execte(query).fetchall())

cur.close
conn.close()
