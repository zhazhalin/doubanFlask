from flask import Flask,render_template
import sqlite3
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index')
def home():
    # return render_template("index.html")
    return index()

@app.route('/movie')
def movie():
    datalist=[]
    conn=sqlite3.connect("豆瓣top250.db")
    cur=conn.cursor()
    sql="select * from movie "
    data=cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template("movie.html",movies=datalist)

@app.route('/score')
def score():
    score=[]
    num=[]
    conn=sqlite3.connect("豆瓣top250.db")
    cur=conn.cursor()
    sql='''
        select score,count(score) from movie group by score
    '''
    data=cur.execute(sql)
    for item in data:           #循环输出
        score.append(item[0])
        num.append(item[1])
    cur.close()
    conn.close()
    return render_template("score.html",score=score,num=num)        #接入参数

@app.route('/team')
def team():
    return render_template("team.html")

@app.route('/word')
def word():
    return render_template("word.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
