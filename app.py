import sqlite3
import pickle
import sys
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

import os

app = Flask(__name__)
app.secret_key = 'Group_1_Raj_the_leader'

# Create SQLite capstone and table
conn = sqlite3.connect('capstonedb.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              username TEXT UNIQUE,

              password TEXT)''')
conn.commit()
conn.close()






# Function to hash the password
def hash_password(password):
    return generate_password_hash(password)

# Function to verify hashed password
def verify_password(hashed_password, password):
    return check_password_hash(hashed_password, password)

# ... (existing code)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        # role = request.form['role']
        password = request.form['password']

        # Hash the password
        hashed_password = hash_password(password)

        conn = sqlite3.connect('capstonedb.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (username,  password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        conn.close()

        return render_template('login.html')

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('capstonedb.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=?", (username,))
        user = c.fetchone()
        conn.close()

        if user and verify_password(user[2], password):
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return 'Invalid credentials. Please try again.'

    return render_template('login.html')



@app.route('/')
def home():
    username = session.get('username')
    if username:
        return render_template('index.html')
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


# @app.route('/api/historical_data/')
# def historical_data():
#     conn = sqlite3.connect('capstonedb.db')
#     c = conn.cursor()
#     buddy = c.execute("SELECT * FROM dataset ORDER BY id DESC LIMIT 7")
#     conn.commit()
#     conn.close()

#     return {
#         "RESULTS" : buddy
#     }


# historical_data()


@app.route('/api/ucsvsr_model', methods=['GET', 'POST'])
def UCS_Pred():
    if request.method == 'POST':
        Density = request.form['Density']
        Depth = request.form['Depth']
        UCS = request.form['UCS']

        with open('models/ucsvsr.pkl','rb') as f:
            ucsvsr_model = pickle.load(f)
            print('printed value  ', ucsvsr_model.predict([[Density, Depth, UCS]]))


        conn = sqlite3.connect('capstonedb.db')
        c = conn.cursor()
        c.execute("INSERT INTO UCS_virginStress (Density, Depth, UCS) values (?, ?, ?)", (Density, Depth, UCS))
        conn.commit()
        conn.close()

        return render_template('index.html')



   
        # return ucsvsr_model.predict([[11, 43, 55]])


# UCS_Pred()





if __name__ == '__main__':
    app.run(debug=True)
