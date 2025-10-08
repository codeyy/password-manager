import sys
import os
from flask import Flask, request, jsonify, render_template, session, redirect
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from security import gen_salt, derive_key, encrypt_data, decrypt_data
import time



conn = sqlite3.connect('passvault.db', check_same_thread=False)
db = conn.cursor()


app = Flask(__name__)
app.secret_key = '7712d3f4e5b6a7c8d9e0f1a2b3c4d5e6'  # Replace with a secure key in production
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/')
def home():
    if not session.get('user_id'):
        return redirect('/login')

    entry = db.execute("SELECT service, username, category FROM passwords WHERE user_id = ?", (session['user_id'],))
    entries = entry.fetchall()

    return render_template('dashboard.html', entries=entries)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db.execute("SELECT id, hashed_password, salt FROM users WHERE username = ?", (username,))
        user = db.fetchone()

        if user and check_password_hash(user[1], password):  # Replace with actual hash check
            session['user_id'] = user[0]
            return redirect('/')
        else:
            return "Invalid credentials", 401

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Add user registration logic here (e.g., save to database)
        hashed_password = generate_password_hash(password)  # Replace with actual hashing
        salt = gen_salt()

        # Save username and hashed_password to database
        db.execute("INSERT INTO users (username, hashed_password, salt) VALUES (?, ?, ?)", (username, hashed_password, salt))
        conn.commit()

        return redirect('/login')
    return render_template('register.html')

@app.route('/add-password', methods=['GET', 'POST'])
def add_password():
    if request.method == 'POST':

        service = request.form['service'].upper()
        username = request.form['username']
        password = request.form['password']
        category = request.form['category'].upper()
        master_password = request.form['master_password']
        db.execute("SELECT username, hashed_password, salt FROM users WHERE id = ?", (session['user_id'],))
        user = db.fetchone()
        salt = user[2]

        if user and check_password_hash(user[1], master_password):

            # encrypt the password before saving
            encrypted_password = encrypt_data(derive_key(master_password,salt), password)
            db.execute("INSERT INTO passwords (user_id, service, username, password_encrypted, category) VALUES (?, ?, ?, ?, ?)",
                       (session['user_id'], service, username, encrypted_password, category))
            conn.commit()

            return redirect('/')
        else:
            return redirect('/logout')

    elif request.method == 'GET':
        return render_template('add_password.html')

@app.route('/passwords', methods=['GET', 'POST'])
def passwords():
    if not session.get('user_id'):
        return render_template('error.html', error="401 Unauthorized")
    if request.method == 'POST':
        password = request.form['password']

        db.execute("SELECT username, hashed_password FROM users WHERE id = ?", (session['user_id'],))
        user = db.fetchone()
        username = user[0]
        if user and check_password_hash(user[1], password):  # Replace with actual hash check
            salt = db.execute("SELECT salt FROM users WHERE username = ?", (username,)).fetchone()[0]
            entry = db.execute("SELECT service, username, password_encrypted, category, updated_at FROM passwords WHERE user_id = ?", (session['user_id'],))
            entries = entry.fetchall()
            decrypted_entries = []
            for e in entries:
                decrypted_password = decrypt_data(derive_key(password,salt), e[2])
                decrypted_entries.append((e[0], e[1], decrypted_password, e[3], e[4]))
            return render_template('passwords.html', entries=decrypted_entries)
        else:
            return redirect('/logout')

    elif request.method == 'GET':
        entry = db.execute("SELECT service, username, password_encrypted, category, updated_at FROM passwords WHERE user_id = ?", (session['user_id'],))
        entries = entry.fetchall()
        raw_entries = [(e[0], e[1], "********", e[3], e[4]) for e in entries]
        return render_template('passwords.html', entries=raw_entries)




@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error="404- Not Found"), 404
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', error="500- Internal Server Error"), 500
@app.errorhandler(Exception)
def handle_exception(e):
    return render_template('error.html', error="-An error occurred: " + str(e)), 500

if __name__ == '__main__':
    app.run(debug=True)