FROM python:3.14.6-alpine

COPY requirement.txt /tmp

RUN pip install -r /tmp/requirement.txt

COPY ./src /src

CMD  python /src/app.py