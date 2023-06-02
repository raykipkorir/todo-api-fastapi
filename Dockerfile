# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
FROM python:3.9
WORKDIR /app
# ENV PYTHONPATH "${PYTHONPATH}:/"
# ENV PORT=8000

RUN pip install --upgrade pip

COPY ./requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app

COPY ./entrypoint.sh /app/
ENTRYPOINT [ "sh", "entrypoint.sh" ]
