import pyodbc

# conn = pyodbc.connect('DRIVER={SQL Server};server=DESKTOP-F91KEVI\\SA1;database=pythonDB;uid=username;pwd:password')
conn = pyodbc.connect("DRIVER={SQL Server};server=DESKTOP-F91KEVI\SA1")
cur = conn.cursor()

query = 'select @@version'

print(cur.execute(query).fetchall())

query = "insert into pydb..task(title, description, status) values ('{}', '{}', '{}')"

content = [['get grocery', 'milk products', False],
           ['get grocery1', 'milk products1', False]]

for row in content:
    cur.execute(query.format(*row))

conn.commit()

select_query = 'select * from pydb..task'
cur.execute(select_query)

print([meta[0] for meta in cur.description])

for row in cur.fetchall():
    print(row)

cur.close
conn.close()
