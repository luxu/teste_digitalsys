ARG PYTHON_VERSION=3.11-slim-buster

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements/local.txt ./requirements/local.txt

RUN set -ex && \
    pip install -U pip && \
    pip install --no-cache-dir -r requirements\dev.txt

COPY . /app/

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "emprestimo.wsgi"]