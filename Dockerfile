FROM python:3.9-slim-buster

COPY . /app
WORKDIR /app

RUN pip3 install poetry==1.1.8
RUN poetry install
RUN poetry run pytest
CMD poetry run python3 dapp/main.py