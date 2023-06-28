FROM python:3.11-slim

RUN mkdir /code
WORKDIR /code

RUN apt update -y \
    && apt install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    wait-for-it \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

ADD requirements.txt /code/

RUN pip install -U pip && \
    pip install --no-cache-dir -r requirements.txt

ADD . /code/

# create unprivileged user
RUN adduser --disabled-password --gecos '' myuser

#EXPOSE 8000

#CMD [ "gunicorn", "--bind", ":8000", "emprestimo.wsgi" ]