from flask import render_template, request, redirect, session

from flask_app.models import dojo

from flask_app import app

@app.route('/')
def index():
    return render_template('/index.html') 

@app.route('/save', methods=["POST"])
def save():
    if not dojo.Dojo.validate_survey(request.form):
      return redirect('/')
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