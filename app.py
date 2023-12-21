from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# SQLite数据库配置
DATABASE = 'database/question.db'

def connect_db():
    return sqlite3.connect(DATABASE)

# 查询数据库函数
def query_database(keyword):
    conn = connect_db()
    cursor = conn.cursor()

    # 在这里根据你的表名和字段名进行调整
    cursor.execute("SELECT ISSUE, CHOICE, ANSWER FROM QUESTIONS WHERE ISSUE LIKE ?", ('%' + keyword + '%',))

    records = cursor.fetchall()

    conn.close()
    return records

# 定义路由
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        keyword = request.form['keyword']
        records = query_database(keyword)
        return render_template('index.html', keyword=keyword, records=records)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
