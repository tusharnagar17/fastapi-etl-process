FROM python:3.12-alpine AS base

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

##
## Development build
FROM base AS development

EXPOSE 80

CMD ["fastapi","dev", "main.py", "--host","0.0.0.0","--port", "80"]


##
## Production build
FROM base AS production

EXPOSE 80

CMD ["fastapi", "run", "main.py", "--host","0.0.0.0", "--port", "80"]

