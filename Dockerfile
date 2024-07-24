ARG PYTHON_VERSION=3.11.9
FROM --platform=linux/amd64 python:${PYTHON_VERSION}-slim as base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

RUN pip install poetry

COPY pyproject.toml poetry.lock* /app/

RUN --mount=type=cache,target=/root/.cache/pip \
    poetry install --no-root --only main

USER appuser

COPY . .

EXPOSE 8000

CMD ["python", "main.py"]
