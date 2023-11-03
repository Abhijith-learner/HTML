from flask import Flask, render_template,redirect,url_for


app = Flask(__name__)

@app.route('/')
def Home():
    # return render_template("home.html")
    return render_template('index.html')

@app.route("/passed/<int:score>")
def passed(score):
    return 'Congratulations!!  your passed . Score ='+str(score)

@app.route("/fail/<int:score>")
def fail(score):
    return 'DAMN!!  your failed! . Score ='+str(score)

@app.route('/result/<int:marks>')
def result(marks):
    result =''
    if marks<40:
        result='fail'
    else:
        result='passed'

    print('Boom:',url_for(result,score=marks))    
    return redirect(url_for(result,score=marks))

if __name__=='__main__':
    app.run(debug=True)