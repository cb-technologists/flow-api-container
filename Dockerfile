FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN pip install pipenv

COPY Pipfile Pipfile.lock /usr/src/app/

RUN pipenv install --system

COPY . .

CMD [ "python", "./flow_rest.py" ]
