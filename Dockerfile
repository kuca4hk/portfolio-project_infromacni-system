ARG VIRTUAL_ENV=/opt/venv
FROM python:3.10-slim AS base
RUN apt update && apt -y install curl gcc

FROM base AS build
ARG VIRTUAL_ENV

RUN python -m venv ${VIRTUAL_ENV}
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"

# upgrade pip to latest
RUN pip install --upgrade pip wheel

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

FROM base AS final
ARG VIRTUAL_ENV
ENV PYTHONBUFFERED=1

RUN useradd -u 1000 app

WORKDIR /app
USER app

COPY --from=build --chown=1000:1000 ${VIRTUAL_ENV} ${VIRTUAL_ENV}
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"

COPY --chown=1000:1000 . .


EXPOSE 8000