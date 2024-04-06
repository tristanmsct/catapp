FROM python:3.11-slim

ARG APP_PATH=/catmonitor/
ARG APP_USER=catmonitor
WORKDIR ${APP_PATH}

RUN apt-get update && apt-get upgrade -y \
	&& rm -rf /var/lib/apt/lists/* \
	&& adduser --system --group --uid 1000 --home ${APP_PATH} ${APP_USER} \
	&& pip install --no-cache-dir 'poetry>=1.6' \
	&& poetry config virtualenvs.create false

COPY --chown=${APP_USER}:${APP_USER} catmonitor/pyproject.toml catmonitor/poetry.lock ./
COPY --chown=${APP_USER}:${APP_USER} catmonitor/catmonitor/ ./catmonitor/
RUN touch README.md

RUN poetry install --no-interaction --no-ansi

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8051/_stcode/health

USER ${APP_USER}

ENTRYPOINT [ "streamlit", "run", "catmonitor/catdisplay.py", "--server.port=8501", "--server.address=0.0.0.0" ]
