from flask import Flask, render_template, request, flash
import requests
import smtplib
import os

app = Flask(__name__)
app.config['SECRET_KEY'] =  os.environ.get("FLASK_KEY")


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Email Configuration
        sender_email = ''
        receiver_email = ''
        password = 'vhbjakyjnuouhpyu'

        # Construct the email message
        subject = 'New Message from Contact Form'
        body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        message = f'Subject: {subject}\n\n{body}'

        # Send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(sender_email, password)
            smtp.sendmail(sender_email, receiver_email, message)

        return 'Message sent successfully!'
    else:
        return 'Error!'

if __name__ == '__main__':
    app.run()

    