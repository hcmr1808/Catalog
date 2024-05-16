FROM python:3.11.4-alpine3.18
ENV LANG C.UTF-8

WORKDIR /app

RUN apk add --no-cache libpq gcc python3-dev musl-dev

COPY ./requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./app.py /app/

CMD ["flask", "run", "--host", "0.0.0.0"]