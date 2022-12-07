FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt /app
RUN pip install --upgrade pip && pip install -r /app/requirements.txt --no-cache-dir

COPY . /app

CMD ["python3", "main.py"]