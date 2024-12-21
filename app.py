from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do banco de dados com as mesmas credenciais do CCT EAD
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://vicelmo:qaz123wsx@cct-db:5432/cct'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def home():
    try:
        # Testa a conexão com o banco
        db.session.execute('SELECT 1')
        status = "Conexão com o banco de dados estabelecida com sucesso!"
    except Exception as e:
        status = f"Erro na conexão com o banco: {str(e)}"

    return f"""
    <html>
    <head>
        <title>CCT - Sistema de Teste</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                background-color: #f0f2f5;
            }}
            .container {{
                max-width: 800px;
                margin: 0 auto;
                background-color: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}
            h1 {{
                color: #1a73e8;
                text-align: center;
            }}
            .status {{
                margin-top: 20px;
                padding: 10px;
                border-radius: 4px;
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Bem-vindo ao Sistema CCT</h1>
            <p>Sistema inicializado com sucesso!</p>
            <div class="status">
                <strong>Status do Banco de Dados:</strong>
                <p>{status}</p>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
