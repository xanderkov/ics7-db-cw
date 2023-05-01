FROM python:3.10

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install fastapi sqlalchemy "uvicorn[standard]" psycopg2
COPY . .
CMD [ "python", "./back.py" ]
