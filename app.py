from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Database configuration - usando conexão direta com o serviço do Easypanel
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@cct-db:5432/cct'
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
