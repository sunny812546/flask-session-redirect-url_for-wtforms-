from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, validators,
                     RadioField, TextAreaField, SubmitField)

app = Flask(__name__)

app.config["SECRET_KEY"] = "mykey"


class Form(FlaskForm):
    name = StringField("Enter Name", [validators.DataRequired()])

    submit = SubmitField("submit")


@app.route("/", methods=["POST", "GET"])
def home():
    form = Form()
    if form.validate_on_submit():
        session["name"] = form.name.data
        flash("thank you! {}".format(session["name"]))

        return redirect(url_for("home"))
    return render_template("home.html", form=form)


@app.route("/thankyou", methods=["POST", "GET"])
def thankyou():
    return render_template("thankyou.html")


app.run(debug=True)
