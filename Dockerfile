FROM python:3.9

RUN mkdir -p /usr/src/app

RUN  apt-get update

COPY requirements.txt /usr/src/app/requirements.txt

WORKDIR /usr/src/app

RUN pip install -r requirements.txt

COPY . .


EXPOSE 8000

CMD gunicorn -b :8000 --capture-output --enable-stdio-inheritance store.wsgi

