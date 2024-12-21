FROM python:3.9-alpine

WORKDIR /app

# Install system dependencies
RUN apk add --no-cache \
    postgresql-dev \
    gcc \
    python3-dev \
    musl-dev

# Install Python packages
RUN pip install flask \
    flask-sqlalchemy \
    psycopg2-binary \
    gunicorn

# Copy application code
COPY . .

EXPOSE 3000

CMD ["gunicorn", "--bind", "0.0.0.0:3000", "app:app"]
