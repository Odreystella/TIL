#from flask import flask
from flask import Flask, render_template


app = Flask(__name__)

# serve.string
@app.route('/')
def index():
    #return 'Flask works'
    return render_template('index.html')

#addtional route with json
@app.route('/users')
def show_users():
    return {'users:['John Doe', 'Jane Doe']}


if __name__=='__main__':
    app.run(host='localhost', port=8080, debug=True)