FROM python:3.10-slim

WORKDIR /app

COPY custom_exporter.py .

RUN pip install prometheus_client psutil

EXPOSE 8000

CMD ["python3", "custom_exporter.py"]
