FROM python:3.5.7
MAINTAINER Corey Gillen gillenc@uoregon.edu

COPY app/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY app/main.py /app/main.py
RUN curl https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh -O \
  && chmod +x wait-for-it.sh

CMD ["./wait-for-it.sh", "db-service:3306", "--", "python", "app/main.py"]
