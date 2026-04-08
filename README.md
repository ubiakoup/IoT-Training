# Smart Factory IoT – Edge to Cloud (IT/OT + DevOps)

## Overview

This training provides a complete implementation of an industrial IoT architecture, from the Operational Technology (OT) layer to the Cloud.

It covers the full lifecycle of an IoT system:
- Data generation (PLC simulation)
- Data collection and processing (Edge Gateway)
- Real-time monitoring
- Cloud integration
- DevOps automation

The goal is to build a production-ready architecture used in modern Industry 4.0 environments.

---

## Architecture

The system is structured into three main layers:

### OT Layer
Simulation of industrial systems (PLC):
- Motor system
- Hydraulic system
- Energy system

Data is exposed using OPC-UA.

---

### Edge Layer (Raspberry Pi)

The Edge Gateway is responsible for:
- Collecting data from OPC-UA
- Publishing data through MQTT
- Processing data using Node-RED
- Storing data in InfluxDB
- Visualizing data with Grafana

All components are containerized using Docker.

---

### Cloud Layer

Integration with AWS:
- AWS IoT Core (secure MQTT ingestion)
- S3 (data storage)
- SNS (notifications)

---

## DevOps Strategy

The deployment strategy follows three phases:

### Provisioning (Ansible)
- Installation of Docker and dependencies
- Initial deployment of the stack

### Runtime (Docker)
- Execution of all services in containers

### Update (Pull Model)
- The Edge device automatically retrieves updates
- Uses Git to pull new versions
- Redeploys services using Docker Compose

Optional:
- CI/CD pipeline for building and validating Docker images

---

## Training Structure

The training is organized into progressive hands-on labs:

### Phase 1 – Fundamentals
- Architecture overview
- OT setup
- Edge Gateway setup

### Phase 2 – IoT Pipeline
- OPC-UA
- MQTT
- Node-RED
- InfluxDB
- Grafana

### Phase 3 – DevOps
- Docker
- Docker Compose
- Ansible
- Pull Model

### Phase 4 – Cloud
- AWS IoT Core
- Data ingestion
- Node-RED and Python approaches

### Phase 5 – Advanced & Final Project
- CI/CD automation
- Full system simulation
- Final architecture review

---

## Learning Outcomes

At the end of this training, participants will be able to:

- Design an industrial IoT architecture
- Implement a complete Edge-to-Cloud pipeline
- Deploy and manage IoT systems using DevOps practices
- Secure communication using TLS and certificates
- Integrate IoT systems with cloud platforms

---

## Target Audience

- DevOps engineers
- IoT engineers
- Industrial engineers
- Software engineers interested in Industry 4.0

---

## Key Technologies

- OPC-UA
- MQTT
- Node-RED
- InfluxDB
- Grafana
- Docker
- Ansible
- AWS IoT Core

---

## Conclusion

This training goes beyond basic IoT projects by combining:

- Industrial protocols (OPC-UA)
- Edge computing
- Cloud integration
- DevOps practices

It provides a realistic and production-oriented approach to IoT systems.
