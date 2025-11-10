FROM python:3.10
WORKDIR /app
COPY custom_exporter.py .
RUN pip install prometheus_client requests
CMD ["python3", "custom_exporter.py"]
