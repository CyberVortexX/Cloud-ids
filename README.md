<div align="center">

# 🛡️ Cloud-Based Intrusion Detection System

**Real-time network threat detection powered by Apache Kafka, Machine Learning, and the ELK Stack — deployed on AWS.**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Apache Kafka](https://img.shields.io/badge/Apache_Kafka-231F20?style=flat-square&logo=apachekafka&logoColor=white)
![Elasticsearch](https://img.shields.io/badge/Elasticsearch-005571?style=flat-square&logo=elasticsearch&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![AWS](https://img.shields.io/badge/AWS_EC2-FF9900?style=flat-square&logo=amazonaws&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)

</div>

---

## 📖 Overview

This project is a cloud-native Intrusion Detection System (IDS) that ingests live network traffic, streams it through an Apache Kafka pipeline, runs it through an ML anomaly detection model, and visualizes results in real time on a Kibana dashboard — all containerized with Docker and hosted on AWS EC2.

---

## 🏗️ Architecture

```
Traffic Generator
      │
      ▼
 Kafka Producer  ──►  Kafka Topic  ──►  Kafka Consumer
                                               │
                                               ▼
                                    ML Detection Engine
                                    (Isolation Forest)
                                               │
                                               ▼
                                       Elasticsearch
                                               │
                                               ▼
                                      Kibana Dashboard
```

---

## ✨ Features

- **Real-time ingestion** — continuous network traffic simulation and capture
- **Kafka streaming pipeline** — fault-tolerant, high-throughput event streaming via Zookeeper + Kafka
- **ML-based anomaly detection** — unsupervised Isolation Forest model flags abnormal traffic patterns
- **Elasticsearch indexing** — fast, scalable storage and querying of all traffic events
- **Kibana dashboards** — live visual monitoring of attacks, protocols, ports, and source IPs
- **Fully containerized** — one-command deployment with Docker Compose

---

## 🗂️ Project Structure

```
cloud-ids/
├── docker-compose.yml        # Orchestrates all services
├── ml/
│   └── ids_model.py          # Isolation Forest anomaly detection
└── streaming/
    ├── producer.py            # Kafka producer — publishes traffic events
    └── consumer.py            # Kafka consumer — feeds ML engine & Elasticsearch
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Cloud Infrastructure | AWS EC2 |
| Containerization | Docker, Docker Compose |
| Message Streaming | Apache Kafka, Zookeeper |
| ML Detection | Python, Scikit-Learn (Isolation Forest) |
| Storage & Search | Elasticsearch |
| Visualization | Kibana |

---

## 🚀 Getting Started

### Prerequisites

- Docker & Docker Compose installed
- AWS EC2 instance (or local machine for testing)
- Python 3.10+

### 1. Clone the repository

```bash
git clone https://github.com/CyberVortexX/cloud-ids.git
cd cloud-ids
```

### 2. Start all services

```bash
docker-compose up -d
```

This spins up Zookeeper, Kafka, Elasticsearch, and Kibana in the background.

### 3. Run the traffic producer

```bash
python streaming/producer.py
```

### 4. Start the consumer and ML detection engine

```bash
python streaming/consumer.py
```

### 5. Open the Kibana dashboard

Navigate to `http://localhost:5601` in your browser.

---

## 📊 Kibana Dashboard

The dashboard provides a live view of network activity and detected threats:

| Panel | Description |
|---|---|
| 🔴 Top Attacking IPs | Ranks source IPs by volume of flagged events |
| 📡 Protocol Distribution | Breakdown of TCP, UDP, ICMP, and other traffic |
| 🎯 Most Targeted Ports | Highlights frequently probed destination ports |
| 📈 Real-Time Traffic Monitor | Rolling timeline of total vs. anomalous traffic |

---

## 🧠 ML Detection Model

The system uses **Isolation Forest**, an unsupervised anomaly detection algorithm well-suited for network intrusion scenarios:

- Trained on baseline normal traffic patterns
- Flags statistical outliers as potential threats
- No labeled attack data required
- Low false-positive rate on stable network baselines

Model logic lives in `ml/ids_model.py`.

---

## 👤 Author

**CyberVortexX**

---

<div align="center">
  <sub>Built with Kafka, ML, and a passion for cybersecurity.</sub>
</div>
