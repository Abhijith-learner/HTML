from flask import Flask, render_template,redirect,url_for,request


app = Flask(__name__)

@app.route('/')
def Home():
    # return render_template("home.html")
    return render_template('index.html')

# @app.route("/passed/<int:score>")
# def passed(score):
#     return 'Congratulations!!  your passed . Score ='+str(score)

# @app.route("/fail/<int:score>")
# def fail(score):
#     return 'DAMN!!  your failed! . Score ='+str(score)

@app.route('/result/<int:marks>')
def result(marks):
    result =''
    if marks<40:
        result='fail'
    else:
        result='passed'

    return render_template('result.html',final=result)

@app.route('/submit',methods=['GET','POST'])
def submit():
    total_score=0
    if request.method=='POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        cpp = float(request.form['cpp'])
        dscience = float(request.form['dscience'])
        total_score=(science+maths+cpp+dscience)/4
        print(total_score)
    res=''
    if total_score>=50:
        res='passed'
    else:
        res='fail'
        
    print(url_for('result',marks=total_score))
    return redirect(url_for('result',marks=total_score))        


if __name__=='__main__':
    app.run(debug=True)