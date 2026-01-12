FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# -u sorgt für unbuffered output, damit logs sofort erscheinen
CMD ["python", "-u", "app.py"]