FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/

# Install system dependencies required for psycopg2 - slim version of python does not have these
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    python3-dev

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 5000

CMD ["python3", "index.py"]