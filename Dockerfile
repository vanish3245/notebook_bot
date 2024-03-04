FROM python:3.12

WORKDIR /app

RUN pip install poetry

COPY ./poetry.lock pyproject.toml ./

RUN poetry install --no-interaction --no-cache --no-root

COPY ./bot ./bot

CMD ["poetry", "run", "python", "-m", "bot"]