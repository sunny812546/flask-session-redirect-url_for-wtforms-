from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, validators,
                     RadioField, TextAreaField, SubmitField)

app = Flask(__name__)

app.config["SECRET_KEY"] = "mykey"


class Form(FlaskForm):
    email = StringField("Enter Email", [validators.DataRequired()])
    feedback = TextAreaField("Write Somethings")
    gender = RadioField("Gender:", choices=[("male", "male"),
                                            ("female", "female")])
    age = BooleanField("are you 18+?")
    submit = SubmitField("submit")


@app.route("/", methods=["POST", "GET"])
def home():
    form = Form()
    if form.validate_on_submit():
        session["email"] = form.email.data
        session["feedback"] = form.feedback.data
        session["gender"] = form.gender.data
        session["age"] = form.age.data
        return redirect(url_for("thankyou"))
    return render_template("home.html", form=form)


@app.route("/thankyou", methods=["POST", "GET"])
def thankyou():
    return render_template("thankyou.html")


app.run(debug=True)
