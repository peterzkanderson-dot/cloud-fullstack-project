# Cloud Full-Stack Energy Monitoring System

## Overview
This project implements an IoT-based energy monitoring pipeline deployed using Docker and cloud-ready infrastructure.

A Python-based simulator generates real-time energy data, which is transmitted via MQTT, processed by an ingestion service, stored in InfluxDB, and visualized through Grafana dashboards.

This system demonstrates how modern IoT and cloud architectures handle real-time data collection, processing, storage, and visualization.

---

## Architecture
The system follows this data pipeline:

Simulator → MQTT Broker → Ingestion Service → InfluxDB → Grafana

- Simulator (Python): Generates real-time energy metrics (voltage, current, power, etc.)
- MQTT (Mosquitto): Enables lightweight real-time messaging
- Ingestion Service (Python): Processes and stores incoming data
- InfluxDB: Time-series database optimized for real-time data
- Grafana: Interactive dashboard for visualization

---

## Features
- Real-time energy data simulation
- MQTT-based messaging system
- Data ingestion and processing using Python
- Time-series data storage with InfluxDB
- Interactive monitoring dashboard with Grafana

---

## Tech Stack
- Python
- Docker & Docker Compose
- MQTT (Eclipse Mosquitto)
- InfluxDB
- Grafana

---

## How to Run

1. Start all services
docker-compose up -d

2. Run the simulator
python simulator.py

3. Run the ingestion service
python ingestion.py

4. Access Grafana dashboard
http://localhost:3000

---

## Example Metrics
The system monitors:
- Voltage
- Current
- Power
- Energy
- Frequency
- Power Factor

---

## Purpose
This project showcases practical skills in:
- Building real-time data pipelines
- Working with IoT communication protocols (MQTT)
- Managing time-series databases
- Creating monitoring dashboards
- Using Docker for service orchestration

---

## Notes
- .env file is excluded from version control for security
- Ensure environment variables are configured before running the project
