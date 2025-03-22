from flask import Flask, render_template, redirect, url_for
import smtplib
import ssl

app = Flask(__name__)

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
SENDER_EMAIL = 'aryanshekar2012@gmail.com'
SENDER_PASSWORD = 'ziwc veph zfdw mdso'  # Use App Password, not Gmail password
RECEIVER_EMAIL = 'aryan.shekar@outlook.com'

def send_email():
    subject = "Hello from Flask App!"
    body = "This email was sent from a Python Flask app by clicking a button."
    message = f"Subject: {subject}\n\n{body}"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def trigger_email():
    send_email()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
