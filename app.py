from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

MAILERSEND_API_KEY = 'YOUR_OWN_MAILERSEND_API'
MAILERSEND_FROM_EMAIL = 'YOUR_EMAIL'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        recipient_email = request.form['email']
        message_body = request.form['message']

        headers = {
            "Authorization": f"Bearer {MAILERSEND_API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "from": {
                "email": MAILERSEND_FROM_EMAIL,
                "name": "m from Flask"
            },
            "to": [
                {"email": recipient_email, "name": "Flask Recipient"}
            ],
            "subject": "📧 Message from m's Flask App",
            "text": message_body
        }

        response = requests.post("https://api.mailersend.com/v1/email", headers=headers, json=data)

        if response.status_code == 202:
            return render_template('index.html', success=True)
        else:
            return render_template('index.html', error=response.text)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
