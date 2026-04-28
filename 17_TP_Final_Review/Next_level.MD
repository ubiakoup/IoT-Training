#  Smart Factory IoT – Edge to Cloud Platform

---

# Vision globale – Genèse du projet

---

## D’où on part

Ce projet s’inspire d’un environnement industriel réel :

```text
Machines (OT) → PLC → données industrielles
```

👉 Exemples :

* température moteur
* vibration
* courant
* vitesse

---

##  Étape 1 — Couche OT (Terrain)

```text
Machines → Automates (PLC) → données
```

👉 Données issues du monde réel industriel

---

##  Étape 2 — Edge Gateway

Pour exploiter ces données, nous avons introduit un **Edge Gateway**.

---

###  Stack Edge (Docker Compose)

```text
Edge Gateway
├── Mosquitto (broker MQTT)
├── Data Collector (Python OPC UA → MQTT)
├── InfluxDB (stockage temps réel)
├── Grafana (visualisation)
├── Node-RED (orchestration)
```

---

###  Rôle de l’Edge

```text
✔ collecter les données OT
✔ les transformer
✔ les visualiser localement
✔ fonctionner sans cloud
```

---

##  Étape 3 — Connexion au Cloud

```text
Edge → AWS IoT Core
```

---

###  Évolution progressive

---

####  TP12 — Pull Model

```text
Edge vérifie les mises à jour (polling)
```

---

####  TP13 — Event-Driven Deployment

```text
Git push → MQTT → Edge → déploiement
```

---

####  TP14 — Data Lake

```text
Edge → AWS IoT → S3
```

👉 stockage des données industrielles

---

####  TP15 — Temps réel

```text
Edge → AWS IoT → Lambda → SNS
```

👉 détection d’anomalies + alertes

---

##  Aujourd’hui

```text
OT → Edge → Cloud → Data → Event Processing
```

---

#  Architecture globale

```text
OT (Machines)
   ↓
Edge Gateway (Docker)
   ↓
AWS IoT Core
   ↓
S3 (Data Lake)
   ↓
Lambda (Processing)
   ↓
SNS (Alerting)
```

---

#  Ce que vous avez construit

```text
✔ passerelle industrielle (Edge Gateway)
✔ pipeline IoT complet
✔ architecture event-driven
✔ système de monitoring temps réel
✔ base data engineering
```

---

#  Évolutions futures

---

##  Data Analytics

👉 interroger les données IoT avec SQL

```text
S3 → requêtes analytiques
```

---

##  Data Engineering

👉 transformer et optimiser les données

```text
JSON → formats optimisés
```

---

## Machine Learning

👉 détecter automatiquement les anomalies

```text
maintenance prédictive
```

---

##  Business Intelligence

👉 visualiser les données pour les décideurs

```text
dashboards métier
```

---

##  Scalabilité avancée

👉 introduction de systèmes de streaming comme Kafka

```text
traitement massif de données
```

---

#  Prochaine formation

##  Kubernetes Edge + Cloud

---

##  Objectif

```text
Edge (Kubernetes) → Cloud (Kubernetes)
```

---

## Vous apprendrez à :

* orchestrer vos services IoT
* scaler votre architecture
* gérer des systèmes distribués
* déployer en production

---

# 🚀 Architecture cible finale

```text
Edge (Kubernetes)
        ↓
AWS IoT Core
        ↓
S3 (Data Lake)
        ↓
Processing
        ↓
Analytics
        ↓
Machine Learning
```

---

#  Valeur professionnelle

Ce projet vous prépare à :

* IoT Engineer
* Cloud Engineer
* Data Engineer
* DevOps Engineer
* ML Engineer

---

#  Message important

```text
Ce projet n’est pas un simple TP.

C’est une base réelle pour construire des systèmes industriels modernes.
```

---

#  Motivation

```text
Vous êtes déjà au-dessus du niveau débutant.
```

👉 La suite vous permettra de devenir :

```text
Ingénieur IoT / Cloud / Data complet
```

---

#  À retenir

```text
L’IoT ne s’arrête pas à connecter des objets.

La vraie valeur est dans :
→ la donnée
→ l’analyse
→ l’intelligence
```

---

# 🚀 Let’s build the future

```text
Smart Factory • IoT • Cloud • Data • AI
```

---
