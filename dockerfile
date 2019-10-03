FROM python:3-alpine

# Install app dependencies
RUN pip install paho-mqtt
RUN pip install utils
RUN pip install db
RUN pip install web.py

EXPOSE  80
CMD ["python", "/src/send.py"]