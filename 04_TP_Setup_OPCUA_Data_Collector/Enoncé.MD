# TP 04 - OPC-UA Client & Data Collector (Containerisé)

---

## Objectifs pédagogiques

À la fin de ce TP, vous serez capable de :

* Comprendre le rôle du Data Collector
* Lire des données OPC-UA
* Publier des données vers MQTT
* Conteneuriser une application Python
* Construire et exécuter une image Docker

---

## Contexte

Dans une architecture IoT moderne :

* les applications tournent dans des conteneurs
* l’Edge Gateway exécute plusieurs services

👉 Ici, nous allons déployer notre Data Collector dans un conteneur Docker.

---

# Architecture

```text
OPC-UA → Data Collector (Docker) → MQTT
```

---

# Partie 1 — Structure du projet

---

Créer les fichiers suivants :

```bash
data_collector.py
requirements.txt
Dockerfile
config.yml
```

---

# Partie 2 — requirements.txt

```text
opcua
paho-mqtt
cryptography
PyYAML
```

---

# Partie 3 — Dockerfile

---

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY data_collector.py .

CMD ["python", "data_collector.py"]
```

---

## Explication

* `FROM` → image de base
* `WORKDIR` → dossier de travail
* `COPY` → copie des fichiers
* `RUN` → installation dépendances
* `CMD` → commande de démarrage

---

# Partie 4 — Configuration (config.yml)

Configurer :

```yaml
opcua:
  url: "opc.tcp://192.168.X.X:4840"

mqtt:
  broker: mosquitto
  port: 1883
```

---

# Partie 5 — Build de l’image Docker

---

```bash
docker build -t data-collector .
```

---

# Partie 6 — Lancer le conteneur

---

```bash
docker run -d --name data-collector \
  --network bridge \
  data-collector
```

---

## Important

Si MQTT est dans Docker :

👉 utiliser le même réseau

---

# Partie 7 — Vérification

---

```bash
docker logs data-collector
```

---

## Résultat attendu

```text
Connected to OPC UA Server
Connected to MQTT broker
Published -> factory/plc1/temperature_motor: 45.2
```

---

# Partie 8 — Concepts clés

---

## Pourquoi containeriser ?

* reproductibilité
* portabilité
* isolation

---

## Avantage

👉 même comportement partout (dev / prod)

---

# Analyse

---

## Exercice 1

Quel est le rôle du Data Collector ?

---

## Exercice 2

Pourquoi containeriser cette application ?

---

## Exercice 3

Que fait le Dockerfile ?

---

## Exercice 4

Pourquoi utiliser MQTT après OPC-UA ?

---

# Résultat attendu

* image Docker créée
* conteneur fonctionnel
* données envoyées vers MQTT

---

# Hints

* vérifier IP OPC-UA
* vérifier MQTT
* vérifier logs Docker
* vérifier réseau Docker

---

# Vision globale

```text
OT → Docker → MQTT
```

---

# Conclusion

Le Data Collector est maintenant containerisé.

👉 Vous êtes maintenant dans une architecture IoT moderne.

Prochaine étape :

👉 Déployer MQTT Broker (Mosquitto)

---
