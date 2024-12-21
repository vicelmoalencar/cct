# CCT - Sistema de Teste

Este é um sistema básico para ser hospedado no Easypanel com integração PostgreSQL.

## Configuração no Easypanel

1. Crie um novo serviço no Easypanel usando o Dockerfile fornecido
2. Configure as seguintes variáveis de ambiente:
   - `DATABASE_URL`: URL de conexão com o PostgreSQL (formato: postgresql://usuario:senha@host:5432/database)

## Estrutura do Projeto

- `app.py`: Aplicação Flask principal
- `templates/`: Diretório com os templates HTML
- `requirements.txt`: Dependências do projeto
- `Dockerfile`: Configuração para build da imagem Docker

## Desenvolvimento Local

1. Clone o repositório:
```bash
git clone https://github.com/vicelmoalencar/cct.git
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente em um arquivo `.env`

4. Execute a aplicação:
```bash
python app.py
```

## Banco de Dados

O sistema utiliza PostgreSQL como banco de dados. Certifique-se de ter um servidor PostgreSQL configurado e acessível.
