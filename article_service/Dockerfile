FROM python:3.11-slim

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

COPY ./article_service .

CMD ["gunicorn", "article_service.wsgi:application", "--bind", "0:8000"]
