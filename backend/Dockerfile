FROM python:alpine3.7
COPY ./requirements.txt ./app/
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 5000
CMD python ./waitress_server.py
