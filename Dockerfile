FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 1883

ENV PYTHONUNBUFFERED 1

CMD ["python", "main.py"]