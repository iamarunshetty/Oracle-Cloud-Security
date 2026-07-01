FROM python:3.11-slim

WORKDIR /app

# Install system deps for pyodbc (SQL Server ODBC driver)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    unixodbc-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--port", "8000"]
