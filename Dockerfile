FROM python:3.11-slim

WORKDIR /app

COPY ./reqs.txt /app/reqs.txt

RUN pip install -r reqs.txt

COPY . /app

CMD ["fastapi", "run", "app/main.py", "--port", "8000"]
