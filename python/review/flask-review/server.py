# from flask import flask
from flask import Flask, render_template
# 설치한 Flask 패키지에서 Flask모듈을 import하여 사용
# 가상환경 socket-practice391 실행해야 함



app = Flask(__name__) # Flask생성하고 app변수에 flask 초기화하여 실행

# serve.string
@app.route('/') # 사용자에게 ()에 있는 경로를 안내해준다고 생각
def index():
    #return 'Flask works'
    #return render_template('index.html')
    msg = 'This is msg block'
    return render_template('index.html', msg=msg)
    # 누군가가 / 경로를 요청하여 index함수를 실행하고 
    # render_template 결과를 보여줌

#addtional route with json
@app.route('/users')
def show_users():
    return {'users':['John Doe', 'Jane Doe']}

#route with variable
@app.route('/user/<username>')
def show_user(username):
    return {'user':username}


if __name__=='__main__':
    app.run(host='localhost', port=8080, debug=True)