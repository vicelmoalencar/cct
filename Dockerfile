FROM python:3.9-alpine

WORKDIR /app

# Install Flask and Gunicorn
RUN pip install flask gunicorn

# Copy application code
COPY . .

EXPOSE 3000

CMD ["gunicorn", "--bind", "0.0.0.0:3000", "--workers", "1", "app:app"]
