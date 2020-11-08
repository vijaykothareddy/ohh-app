# from app import app
# from app import run
from flask import Flask, request, render_template
import run

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('my-form.html')
@app.route('/index', methods=['POST'])
def index_post():
    id = request.form['text']
    id = int(id)
    resp = run.drive(id)
    return resp
    #return id

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run()