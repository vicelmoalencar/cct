from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Database configuration with fallback
database_url = os.getenv('DATABASE_URL')
if database_url is None:
    database_url = 'postgresql://postgres:postgres@db:5432/cct'
    print(f"Warning: DATABASE_URL not set, using default: {database_url}")

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def home():
    try:
        # Test database connection
        db.session.execute('SELECT 1')
        db_status = "Database connection successful!"
    except Exception as e:
        db_status = f"Database connection failed: {str(e)}"
    
    return render_template('index.html', db_status=db_status)

if __name__ == '__main__':
    # Create tables
    with app.app_context():
        db.create_all()
    
    # Run the app
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
