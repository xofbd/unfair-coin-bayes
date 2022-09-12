FROM python:3.8.6-slim
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
COPY . /app
WORKDIR /app
EXPOSE 8000
CMD ["bin/run", "prod", "0.0.0.0"]
