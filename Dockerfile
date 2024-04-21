FROM python:3.11
COPY . /app
WORKDIR /app
RUN pip install -t requirements.txt
EXPOSE $PORT
CMD ["flask", "run", "--host=0.0.0.0"]