FROM python:slim-buster as base

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "request.py"]