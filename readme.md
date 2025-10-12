# 🔐 VaultLock

VaultLock is a **secure password manager web app** built as my **CS50 Final Project**.
It allows users to register, log in securely, and manage their saved passwords — all encrypted and stored safely in a local SQLite database.

---

## 🚀 Features

- **User Authentication** — Secure login & registration using hashed passwords.
- **AES Encryption** — Passwords are encrypted using AES before storage.
- **Add / View / Delete Passwords** — Manage credentials by service name, username, and category.
- **Error Handling** — Custom error pages for all exceptions.
- **Modern UI** — A dark, minimal cyber-inspired design with smooth glassmorphism and particle animation.
- **Persistent Sessions** — Keeps users logged in until they logout.

---

## 🖥️ Tech Stack

- **Frontend:** HTML, CSS, Bootstrap
- **Backend:** Python (Flask)
- **Database:** SQLite3
- **Encryption:** Python’s `cryptography` library (Fernet / AES) in security.py
- **Other:** Jinja2 Templates

---

## 📦 Project Structure

project/
├── app.py
├── security.py
├── requirements.txt
├── README.md
├── /static
│ ├── style.css
│ ├── favicon.ico
│ ├── favicon.png
│ └── BACKGROUND.jpg
├── /templates
│ ├── layout.html
│ ├── register.html
│ ├── login.html
│ ├── dashboard.html
│ ├── add_password.html
│ ├── passwords.html
│ └── error.html
└── passvault.db

---

## ⚙️ Installation & Setup

###
1️⃣ Clone the repository
```bash
git clone https://github.com/agam027/project.git
cd project

2️⃣ Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the app
flask run


Then open your browser and go to:

http://127.0.0.1:5000/



🔑 Security Notes:

Passwords are never stored in plaintext.

Each user’s vault is encrypted with a derived key using a Key Derivation Function (KDF) and a per-user salt.

Flask’s session cookies are secured with a random secret key.

🧠 Learning Outcome

This project helped me explore:

Flask routing and Jinja2 templating

Secure password hashing & encryption

Database CRUD operations

Frontend polish with CSS and UI/UX design

Exception handling and Flask error decorators



🧑‍💻 Author
-`Agam Kumar`
CS50x 2025 Final Project

[github](https://github.com/agam027)