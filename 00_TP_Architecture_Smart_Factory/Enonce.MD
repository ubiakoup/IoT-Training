# TP 00 - Découverte de l’architecture Smart Factory

---

## 🎯 Objectifs pédagogiques

À la fin de ce TP, vous serez capable de :

- Comprendre ce qu’est une architecture IoT industrielle
- Identifier les différentes couches (OT, Edge, Cloud)
- Comprendre le flux de données de bout en bout
- Identifier les technologies utilisées dans le projet

---

## Contexte

Dans l’industrie moderne (Industry 4.0), les machines produisent en continu des données.

Ces données doivent être :

- collectées
- traitées
- stockées
- visualisées
- exploitées dans le cloud

Dans ce projet, nous allons simuler une **Smart Factory** complète, de la machine jusqu’au cloud.

---

## Architecture globale



L’architecture du projet est composée de 3 couches principales :

### 1. Couche OT (Operational Technology)

Elle représente le monde industriel :

- machines
- capteurs
- automates (PLC)

👉 Dans notre projet :

- simulation de PLC avec Python
- exposition des données via OPC-UA

---

### 2. Couche Edge (Gateway)

Elle joue le rôle d’intermédiaire entre OT et IT.

👉 Elle permet de :

- collecter les données
- transformer les données
- stocker localement
- visualiser en temps réel

👉 Technologies utilisées :

- Raspberry Pi
- Docker
- MQTT (Mosquitto)
- Node-RED
- InfluxDB
- Grafana

---

### 3. Couche Cloud

Elle permet de :

- centraliser les données
- analyser à grande échelle
- générer des alertes

👉 Technologies :

- AWS IoT Core
- S3
- SNS

---

## Flux de données

Voici le chemin des données dans le système :

```text
PLC → OPC-UA → Data Collector → MQTT → Node-RED → InfluxDB → Grafana
                                                      ↓
                                                   Cloud
