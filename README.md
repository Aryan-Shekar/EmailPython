# EmailPython

📬 Flask Email Sender with Mailersend API
A simple Flask web application that allows users to:

Enter an email address

Type a message

Click a button to send the email via the Mailersend API

🚀 Features
Easy-to-use form interface

Sends custom message to any email

Uses verified domain from Mailersend

Simple Flask + HTML app structure

📁 Project Structure
bash
Copy
Edit
email_flask_app/
├── app.py                  # Flask backend logic
├── templates/
│   └── index.html          # Web form interface
└── README.md               # You're here!
🔧 Setup Instructions
1. Clone or Download the Project
bash
Copy
Edit
git clone https://github.com/your-username/email-flask-app.git
cd email-flask-app
2. Create a Virtual Environment (Optional but recommended)
bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# or
.venv\Scripts\activate      # Windows
3. Install Dependencies
bash
Copy
Edit
pip install flask requests
4. Add Your Mailersend API Info
In app.py, update the following:

python
Copy
Edit
MAILERSEND_API_KEY = 'your_mailersend_api_key'
MAILERSEND_FROM_EMAIL = 'noreply@your-verified-domain.com'
📌 Your from email must be from a verified domain in Mailersend.

🧪 Run the App
bash
Copy
Edit
python app.py
Visit: http://127.0.0.1:5000

✨ Example Usage
Enter an email address (like test@example.com)

Type your message

Click Send Email

If successful, you'll see a ✅ confirmation message

🛠 To Do
Add email validation

Support HTML emails

Add file attachments

Deploy to Heroku or Render

📄 License
This project is open source and free to use under the MIT License.
