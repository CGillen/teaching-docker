FROM python:3.5.7
MAINTAINER Corey Gillen gillenc@uoregon.edu

COPY app/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY app/main.py /app/main.py

CMD [ "python", "/app/main.py" ]
