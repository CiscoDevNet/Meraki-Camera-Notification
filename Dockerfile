FROM python:3.6.7-alpine

ADD . /opt/

WORKDIR /opt/

RUN pip3 install -r requirements.txt


ENTRYPOINT ["python3", "./app.py"]
