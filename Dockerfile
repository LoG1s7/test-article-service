FROM python:3.10-slim

WORKDIR /data

RUN pip install --upgrade pip

COPY ./article_service requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

COPY ./article_service .

CMD ["gunicorn", "article_service.wsgi:application", "--bind", "0:8000"]
