# FROM python:3.8.12
FROM ubuntu:latest
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN \
    apt update && \
    apt install -y pcmanfm featherpad lxtask xterm
ENV DISPLAY=host.docker.internal:0.0
CMD pcmanfm
CMD ["python", "main.py"]
