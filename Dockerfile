FROM python:3.12

ENV APP_HOME=/opt
ENV PYTHONPATH=$APP_HOME
WORKDIR $APP_HOME

RUN apt-get update && \
    apt-get install -y python3-distutils python3-setuptools curl build-essential libpq-dev && \
    rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-interaction --no-ansi

COPY metakam ./metakam

WORKDIR $APP_HOME/metakam

EXPOSE 8000

CMD ["bash", "-c", "echo 'Starting migrations...' && python manage.py migrate && python manage.py collectstatic --noinput && echo 'Starting server...' && python manage.py runserver 0.0.0.0:8000"]
