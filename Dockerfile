FROM python:3.7.2-slim
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
COPY . /app
WORKDIR /app
EXPOSE 5000
CMD ["bin/run.sh", "0.0.0.0"]
