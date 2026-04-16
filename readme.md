##### ⚠️ THIS PROJECT IS NOT MAINTAINED, HENCE DEPRECATED.
Please use [Password-Manager-PRO](https://github.com/codeyy/Password-Manager-PRO) for the latest features.

# Password-Manager (legacy)

> This is a **secure password manager web app**.
It allows users to register, log in securely, and manage their passwords — all encrypted and stored safely in a local SQLite database.

---

## 🚀 Features

- **User Authentication** — Secure login & registration using hashed passwords.
- **AES Encryption** — Passwords are encrypted using AES(Advanced Encryption Standard) before storage.
- **Add / View / Delete Passwords** — Manage credentials by service name, username, and category.
- **Error Handling** — Custom error pages for all exceptions.
- **Modern UI** — A dark, minimal cyber-inspired design with smooth glassmorphism and particle animation.
- **Persistent Sessions** — Keeps users logged in until they logout.

---

## 🖥️ Tech Stack

- **Frontend:** HTML, CSS, Javascript
- **Backend:** Python (Flask framework)
- **Database:** SQLite3
- **Encryption:** Python’s `cryptography` with (AES) in security.py
- **Other:** Jinja2 Templates

---

## ⚙️ Installation & Setup

```
1️⃣ Clone the repository
bash
git clone https://github.com/codeyy/password-manager
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
```


🧑‍💻 Author
-`Agam Kumar`

[GitHub >](https://github.com/codeyy)
