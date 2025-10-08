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
- **Encryption:** Python’s `cryptography` library (Fernet / AES)
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

