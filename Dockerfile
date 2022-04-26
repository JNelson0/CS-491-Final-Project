FROM python:3.8.12
WORKDIR /app
COPY . .
RUN git clone https://github.com/JNelson0/CS-491-Final-Project.git
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
