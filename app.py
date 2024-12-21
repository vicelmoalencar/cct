from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração simplificada do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@cct-db:5432/cct'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def home():
    return "<h1>Bem-vindo ao Sistema CCT</h1><p>Sistema inicializado com sucesso!</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
