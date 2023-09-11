from flask import Flask , render_template , request , url_for


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/count', methods=['GET','POST'])
def count():
    text = request.form['text']
    words = len(text.split())

    text.replace('\r' , '')
    text.replace('\n' , '')
    text.replace(',','')
    
    characters = len(text)
    return render_template('home.html', words=words , characters=characters)

