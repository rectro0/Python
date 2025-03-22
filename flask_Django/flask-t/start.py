from flask import Flask , render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
   return "Welcome"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_f(name=None):
 return render_template('hello.html', person=name)

if __name__ == '__main__':
 app.run(debug=True)