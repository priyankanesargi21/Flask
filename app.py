from flask import Flask, render_template, request, url_for, redirect

#create the flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello World</h1>"

@app.route('/welcome')
def welcome():
    return "Welcome to flask application"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return "the student  passed and the score is "+str(score)
    
    
@app.route('/failure/<int:score>')
def failure(score):
    return "the student failed and the score is "+str(score)


@app.route('/calculate', methods=['POST', 'GET'])
def calculate():
    if request.method=='POST':
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        average_marks = (maths+science+history)/3
        result = ""
        # if average_marks >=50:
        #     result = "success"
        # else:
        #     result = "failure"
        # return redirect(url_for(result, score=average_marks))
        return render_template('calculate.html', results=average_marks)
    else:
        return render_template('calculate.html')
    


#entry point of app
if __name__ =='__main__':
    app.run(debug=True)