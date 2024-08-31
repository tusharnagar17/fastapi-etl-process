FROM python:3.12 AS builder

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY * /app

##
## Development build
FROM python:3.12 AS development

WORKDIR /app

COPY --from=builder /app /app

EXPOSE 80

CMD ['fastapi', 'dev', 'app/main.py', "--port", "80"]

##
## Production build
FROM python:3.12 AS production

WORKDIR /app

COPY --from=builder /app /app

EXPOSE 80

CMD ["fastapi", "run", "app/main.py", "--port", "80"]

