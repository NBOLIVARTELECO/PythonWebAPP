import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from dotenv import load_dotenv
import os
from flask import Flask, render_template, request, redirect, url_for, flash

# Load environment variables
load_dotenv()

# Initialize Flask
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')  # Get secret key from .env

def initialize_firebase():
    """Initialize Firebase Admin SDK"""
    try:
        # Check if already initialized
        firebase_admin.get_app()
    except ValueError:
        # Initialize Firebase Admin SDK with your credentials
        cred = credentials.Certificate("testvscode.json")
        # Get database URL from .env
        firebase_admin.initialize_app(cred, {
            'databaseURL': os.getenv('DATABASE_URL')
        })
    
    return db.reference()

# Initialize Firebase at startup
ref = initialize_firebase()

@app.route('/')
def index():
    # Get all users from Realtime Database
    users = []
    users_ref = ref.child('users')
    users_data = users_ref.get()
    
    if users_data:
        for user_id, user_data in users_data.items():
            user_data['id'] = user_id
            users.append(user_data)
    
    return render_template('index.html', users=users)

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form.get('name')
    email = request.form.get('email')
    
    if name and email:
        # Add user to Realtime Database
        users_ref = ref.child('users')
        new_user_ref = users_ref.push()
        new_user_ref.set({
            'name': name,
            'email': email
        })
    return redirect(url_for('index'))

@app.route('/delete_user/<user_id>', methods=['POST'])
def delete_user(user_id):
    # Delete user from Realtime Database
    ref.child('users').child(user_id).delete()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True) 