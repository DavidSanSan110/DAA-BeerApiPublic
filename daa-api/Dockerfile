FROM python:3.8

WORKDIR /app/daa-api
COPY . .
RUN pip install -r requirements.txt
RUN pip install . --upgrade

CMD ["daa_api"]


