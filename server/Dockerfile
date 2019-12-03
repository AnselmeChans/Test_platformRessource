FROM python:3.6-alpine3.10

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN apk update

RUN apk  add 'py-curl=7.43.0.2-r2'

ADD ./ /

RUN ls *.tar.gz|xargs -I module pip3 install module
RUN rm -f *.tar.gz

RUN pip3 install --upgrade pip && pip3 install -r /requirements.txt


EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


