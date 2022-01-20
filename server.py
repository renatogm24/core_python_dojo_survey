from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template('/index.html') 

@app.route('/save', methods=["POST"])
def save():
    print(request.form)
    print(request.form.getlist("hobbie"))
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comment"] = request.form["comment"]
    session["graduated"] = request.form["graduated"]
    session["hobbie"] = request.form.getlist("hobbie")
    return redirect('/result') 

@app.route('/result')
def result():
    return render_template('/result.html') 


if __name__=="__main__":
  app.run(debug=True)