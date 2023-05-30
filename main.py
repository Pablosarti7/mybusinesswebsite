from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
import smtplib
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Email Configuration
        from_email = email
        
        to_email = os.environ.get('MY_EMAIL')
        to_password = os.environ.get('MY_PASSWORD')

        # Construct the email message
        subject = 'New Message from Contact Form'
        body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        message = f'Subject: {subject}\n\n{body}'

        # Send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(to_email, to_password)
            smtp.sendmail(from_email, to_email, message)
            
        flash("Message Successfully Sent!")
        return render_template("index.html")
    else:
        return 'Error!'

if __name__ == '__main__':
    app.run()
