# https://pastebin.com/raw/8JCFShzM
# https://pastebin.com/raw/Wt8jZLzz
from flask import Flask, jsonify, request
import pyodbc


def get_tasks_from_db():
    conn = pyodbc.connect("DRIVER={SQL Server};server=DESKTOP-F91KEVI\SA1")
    cur = conn.cursor()
    select_query = 'select * from pydb..task'
    cur.execute(select_query)

    column_header = [meta[0] for meta in cur.description]

    content = [dict(zip(column_header, row)) for row in cur.fetchall()]
    cur.close
    conn.close()
    return content


app = Flask(__name__)


@app.route('/todo/tasks', methods=['GET'])
def get_tasks():
    return jsonify(get_tasks_from_db())


@app.route('/todo/tasks', methods=['POST'])
def create_task():
    title = request.json['title']
    status = request.json.get('status', '')
    description = request.json.get('description', '')

    conn = pyodbc.connect("DRIVER={SQL Server};server=DESKTOP-F91KEVI\SA1")
    cur = conn.cursor()
    query = "insert into pydb..task(title, description, status) values ('{}', '{}', '{}')"

    cur.execute(query.format(title, status, description))

    cur.close
    conn.close()

    return jsonify(dict(sucess=True))


if __name__ == '__main__':
    app.run(debug=True)
