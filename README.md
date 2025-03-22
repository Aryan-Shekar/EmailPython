# EmailPython

# 📬 Flask Email Sender with Mailersend API

A simple Flask web application that lets users:

- Enter an email address
- Type a custom message
- Click a button to send the email via the **Mailersend API**

---

## 🚀 Features

- Easy-to-use web form
- Dynamic email sending via Mailersend
- Simple Flask + HTML structure
- No frontend frameworks needed

---

## 📁 Project Structure

email_flask_app/ ├── app.py # Flask backend logic ├── templates/ │ └── index.html # Web form interface └── README.md # You're here!

yaml
Copy
Edit

---

## 🔧 Setup Instructions

### 1. Clone or Download the Project

```bash
git clone https://github.com/your-username/email-flask-app.git
cd email-flask-app
2. (Optional) Create a Virtual Environment
bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# or
.venv\Scripts\activate      # Windows
3. Install Required Packages
bash
Copy
Edit
pip install flask requests
4. Add Your Mailersend API Info
In app.py, replace these with your own values:

python
Copy
Edit
MAILERSEND_API_KEY = 'your_mailersend_api_key'
MAILERSEND_FROM_EMAIL = 'noreply@your-verified-domain.com'
⚠️ The from email must belong to a verified domain on your Mailersend account.

🧪 Running the App
bash
Copy
Edit
python app.py
Then open your browser to:
http://127.0.0.1:5000

✨ How It Works
User enters the recipient’s email and a message

Flask receives the form data on submit

Sends the data to the Mailersend API

Displays a success or error message
