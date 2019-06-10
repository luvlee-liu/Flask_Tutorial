# Pull Base Image
FROM python:3.7.3-alpine3.9

RUN apk add curl

# copy code into image and set as working directory
COPY . /application
WORKDIR /application

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["test.py"]
