import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin.exceptions import FirebaseError
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
    global firebase_initialized, ref
    
    try:
        # Check if already initialized
        firebase_admin.get_app()
        firebase_initialized = True
        ref = db.reference()
        return ref
    except ValueError:
        # Not initialized yet, try to initialize
        try:
            # Check if credentials file exists
            cred_file = "testvscode.json"
            if not os.path.exists(cred_file):
                print(f"⚠️  ADVERTENCIA: Archivo {cred_file} no encontrado.")
                print("   La aplicación funcionará en modo demo sin Firebase.")
                firebase_initialized = False
                return None
            
            # Initialize Firebase Admin SDK with your credentials
            cred = credentials.Certificate(cred_file)
            
            # Get database URL from .env
            database_url = os.getenv('DATABASE_URL')
            if not database_url:
                print("⚠️  ADVERTENCIA: DATABASE_URL no configurada en .env")
                print("   La aplicación funcionará en modo demo sin Firebase.")
                firebase_initialized = False
                return None
            
            firebase_admin.initialize_app(cred, {
                'databaseURL': database_url
            })
            
            firebase_initialized = True
            ref = db.reference()
            print("✅ Firebase inicializado correctamente")
            return ref
            
        except FileNotFoundError:
            print(f"❌ ERROR: Archivo {cred_file} no encontrado.")
            print("   Por favor, asegúrate de tener el archivo de credenciales de Firebase.")
            firebase_initialized = False
            return None
        except Exception as e:
            print(f"❌ ERROR al inicializar Firebase: {str(e)}")
            print("   La aplicación funcionará en modo demo sin Firebase.")
            firebase_initialized = False
            return None
    
    except Exception as e:
        print(f"❌ ERROR inesperado al inicializar Firebase: {str(e)}")
        firebase_initialized = False
        return None

# Initialize Firebase at startup
ref = initialize_firebase()

@app.route('/')
def index():
    # Get all users from Realtime Database
    users = []
    error_message = None
    
    if not firebase_initialized or ref is None:
        error_message = "Firebase no está configurado. Por favor, configura las credenciales de Firebase."
    else:
        try:
            users_ref = ref.child('users')
            users_data = users_ref.get()
            
            if users_data:
                for user_id, user_data in users_data.items():
                    user_data['id'] = user_id
                    users.append(user_data)
        except FirebaseError as e:
            error_code = str(e).lower()
            if 'unauthorized' in error_code or '401' in error_code or 'unauthenticated' in error_code:
                error_message = "Error de autenticación con Firebase. Verifica tus credenciales y las reglas de seguridad de Firebase."
            else:
                error_message = f"Error de Firebase: {str(e)}"
        except Exception as e:
            error_code = str(e).lower()
            if 'unauthorized' in error_code or '401' in error_code or 'unauthenticated' in error_code:
                error_message = "Error de autenticación con Firebase. Verifica tus credenciales y las reglas de seguridad de Firebase."
            else:
                error_message = f"Error inesperado: {str(e)}"
    
    return render_template('index.html', users=users, error_message=error_message, firebase_available=firebase_initialized)

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form.get('name')
    email = request.form.get('email')
    
    if not firebase_initialized or ref is None:
        flash('Firebase no está configurado. No se puede añadir usuarios.', 'error')
        return redirect(url_for('index'))
    
    if name and email:
        try:
            # Add user to Realtime Database
            users_ref = ref.child('users')
            new_user_ref = users_ref.push()
            new_user_ref.set({
                'name': name,
                'email': email
            })
            flash('Usuario añadido correctamente', 'success')
        except FirebaseError as e:
            error_code = str(e).lower()
            if 'unauthorized' in error_code or '401' in error_code or 'unauthenticated' in error_code:
                flash('Error de autenticación con Firebase. Verifica tus credenciales y las reglas de seguridad.', 'error')
            else:
                flash(f'Error de Firebase: {str(e)}', 'error')
        except Exception as e:
            error_code = str(e).lower()
            if 'unauthorized' in error_code or '401' in error_code or 'unauthenticated' in error_code:
                flash('Error de autenticación con Firebase. Verifica tus credenciales y las reglas de seguridad.', 'error')
            else:
                flash(f'Error inesperado: {str(e)}', 'error')
    else:
        flash('Por favor, completa todos los campos', 'warning')
    
    return redirect(url_for('index'))

@app.route('/delete_user/<user_id>', methods=['POST'])
def delete_user(user_id):
    if not firebase_initialized or ref is None:
        flash('Firebase no está configurado. No se puede eliminar usuarios.', 'error')
        return redirect(url_for('index'))
    
    try:
        # Delete user from Realtime Database
        ref.child('users').child(user_id).delete()
        flash('Usuario eliminado correctamente', 'success')
    except FirebaseError as e:
        error_code = str(e).lower()
        if 'unauthorized' in error_code or '401' in error_code or 'unauthenticated' in error_code:
            flash('Error de autenticación con Firebase. Verifica tus credenciales y las reglas de seguridad.', 'error')
        else:
            flash(f'Error de Firebase: {str(e)}', 'error')
    except Exception as e:
        error_code = str(e).lower()
        if 'unauthorized' in error_code or '401' in error_code or 'unauthenticated' in error_code:
            flash('Error de autenticación con Firebase. Verifica tus credenciales y las reglas de seguridad.', 'error')
        else:
            flash(f'Error inesperado: {str(e)}', 'error')
    
    return redirect(url_for('index'))

@app.route('/tutorial')
def tutorial():
    """Vista interactiva de tutorial paso a paso"""
    return render_template('tutorial.html')

@app.route('/practice')
def practice():
    """Vista interactiva de ejercicios prácticos"""
    return render_template('practice.html')

if __name__ == "__main__":
    app.run(debug=True) 