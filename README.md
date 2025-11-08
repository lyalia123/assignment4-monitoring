### Monitoring Stack (Prometheus + Grafana + Custom Exporter)

## Project Description

This project is designed for collecting and visualizing metrics using Prometheus and Grafana.
The system includes three data sources:

Custom Exporter — a Python script that collects weather data from an external API (Open-Meteo).

Postgres Exporter — metrics of the PostgreSQL database.

Node Exporter — system metrics (CPU, RAM, disk, network).

All services are launched using Docker Compose and connected in a single monitoring network.

## Project Setup

Install Docker and Docker Compose.

Make sure docker-compose.yml and prometheus.yml are in the same directory.

Run the command:

docker-compose up --build -d

After starting, the services will be available at:

Prometheus: http://localhost:9090

Grafana: http://localhost:3000
(login: admin / password: admin)

Custom Exporter: http://localhost:8000/metrics

## Dashboard 1 — Custom Exporter (Weather API)

Displays real-time weather data obtained from the Open-Meteo API.
Metrics include temperature, humidity, pressure, cloud cover, wind speed, and direction.

Visualizations:

Overall system load

Resource tracking

Perceived temperature (feels-like)

Comfort index

Average wind speed over the last 5 minutes

Daytime ratio for the past hour

Difference between perceived and actual temperature

Temperature trend

Weather forecast for the next hour

Maximum wind speed in the past 15 minutes

Temperature readings in Celsius

## Dashboard 2 — Database Exporter (PostgreSQL)

Displays the database status and activity.

Visualizations:

Database Growth Over Time

Number of locks

Buffer usage

Temporary file count

Database availability

Read intensity (blocks/sec)

Commit rate (operations/sec)

Transactions per Second (TPS)

Active connections

Database Size (Bytes)

## Dashboard 3 — Node Exporter (System Metrics)

Monitors server performance and system health.

Visualizations:

Network outbound traffic (Mbit/s)

Network inbound traffic (Mbit/s)

Disk space remaining (%)

Free memory (GB)

Load Average (1, 5, 15 minutes)

System uptime (hours)

Disk Usage (%)

Memory Usage (%)

CPU Usage (%)

Disk I/O (Read/Write)

## Verification

Open http://localhost:9090/targets

Ensure all exporters show UP status.

Open http://localhost:8000/metrics

Ensure metrics are updating.

Open Grafana and confirm that the dashboards display data correctly.

## Technologies Used

Python — implementation of the Custom Exporter

Prometheus — metrics collection and storage

Grafana — data visualization

Docker Compose — container orchestration

Open-Meteo API — external weather data source

## Results

After starting the project, Grafana displays three dashboards:

Custom Exporter Dashboard — real-time weather data.

Database Dashboard — PostgreSQL statistics.

Node Exporter Dashboard — server resource monitoring.

The system is fully automated, metrics update every 20 seconds, and are available in Prometheus.
All data is visualized in Grafana and can be used for performance analysis and system monitoring
