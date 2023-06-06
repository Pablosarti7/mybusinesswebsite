from flask import Flask, render_template, request, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
import smtplib
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)

Bootstrap(app)

class LoginForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send Message")

@app.route('/', methods=['GET', 'POST'])
def home():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        message = form.message.data

        # Email Configuration
        from_email = email
        to_email = 'palishpy@gmail.com'
        to_password = 'vhbjakyjnuouhpyu'

        # Construct the email message
        subject = 'New Message from Contact Form'
        body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

        message = f'Subject: {subject}\n\n{body}'

        # Send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(to_email, to_password)
            smtp.sendmail(from_addr=from_email, to_addrs=to_email, msg=message)

        flash('You succesfully sent the message!')
        return redirect(url_for('home'))
    
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run()
