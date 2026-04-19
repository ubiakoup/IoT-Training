# TP 04 — OPC-UA Client & Data Collector (Containerisé)

---

## Objectifs pédagogiques

À la fin de ce TP, vous serez capable de :

- Comprendre le rôle d’un Data Collector dans une architecture IIoT
- Lire des données depuis un serveur OPC UA
- Publier des données vers un broker MQTT
- Comprendre la structure d’une application Python industrielle
- Comprendre la logique de containerisation avec Docker

---

## Contexte

Dans une architecture IoT industrielle :

- les machines (PLC) exposent leurs données via OPC UA
- un service intermédiaire (Data Collector) récupère ces données
- ces données sont ensuite envoyées vers MQTT

👉 Ce Data Collector est généralement exécuté sur un Edge Gateway.

---

# Architecture

```text
OPC-UA → Data Collector → MQTT
````

---

# ⚠️ Étape 0 — Réseau Docker

verifier si le réseau Docker :

```bash
docker network ls
```

---

# Partie 1 — Mise en place du projet

Créer un dossier de travail :

```bash
mkdir data-collector
cd data-collector
```

---

# Partie 2 — Création des fichiers

Créer les fichiers suivants :

```bash
touch data_collector.py
touch requirements.txt
touch Dockerfile
touch config.yml
```

---

# Partie 3 — Travail demandé

Dans ce TP, vous allez **éditer et compléter ces fichiers**.

👉 L’objectif est de comprendre le rôle de chaque composant.

---

## 🔹 1. data_collector.py

Éditer ce fichier pour :

* se connecter au serveur OPC UA
* lire des données (nodes)
* se connecter au broker MQTT
* publier les données

---

## 🔹 2. requirements.txt

Compléter avec les dépendances nécessaires :

* OPC UA
* MQTT
* lecture YAML

---

## 🔹 3. config.yml

Configurer :

* l’adresse du serveur OPC UA
* les paramètres MQTT

---

## 🔹 4. Dockerfile

Créer un Dockerfile permettant :

* d’installer les dépendances
* de copier uniquement les fichiers nécessaires
* de lancer le script

---

# ⚠️ Contraintes importantes

* Ne pas utiliser `COPY . .`
* Copier uniquement les fichiers nécessaires
* Respecter une structure propre

---

# Partie 4 — Build de l’image

```bash
docker build -t data-collector .
```

# Partie 5 — Lancer le Data Collector

```bash
docker run -d \
  --name data-collector \
  --network iiot-network \
  data-collector
```

---

# Partie 7 — Vérification

```bash
docker logs data-collector
```

---

# Résultat attendu

```text
Connected to OPC UA Server
Connected to MQTT broker
Published -> factory/plc1/temperature_motor: 45.2
```

---

# Analyse

---

## Exercice 1

Quel est le rôle du Data Collector dans cette architecture ?

---

## Exercice 2

Pourquoi utilise-t-on un fichier de configuration (config.yml) ?

---


## Exercice 3

Quel est le rôle de MQTT après OPC UA ?

---

# Hints

* vérifier l’adresse OPC UA (192.168.56.11)
* vérifier le réseau Docker
* vérifier les logs
* vérifier que MQTT est actif

---

# Vision globale

```text
Machine → OPC-UA → Data Collector → MQTT → Applications
```

