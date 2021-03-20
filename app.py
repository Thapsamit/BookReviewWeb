from flask import Flask,render_template,url_for,request

app = Flask(__name__)



@app.route('/')

def index():
    return render_template('index.html')

@app.route('/register')

def register():
    return render_template('register.html')



@app.route('/login')

def login():
    return render_template('login.html')


    
@app.route('/dashboard')

def dashboard():
    return render_template('dashboard.html')

@app.route('/dashboard/search')
def search():
    return render_template('search.html') 

@app.route('/dashboard/profile')
def profile():
    return render_template('profile.html')

@app.route('/info/<string:isbn>')
def info(isbn):
    return render_template('info.html')

if __name__ == '__main__':
    app.run(debug=True)

