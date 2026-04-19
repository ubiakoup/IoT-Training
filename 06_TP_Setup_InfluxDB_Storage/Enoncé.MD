# TP 07 — InfluxDB : Stockage des données IoT (Node-RED → Database)

---

## Objectifs pédagogiques

À la fin de ce TP, vous serez capable de :

* Comprendre le rôle d’une base de données time-series
* Comprendre pourquoi InfluxDB est utilisé en IoT
* Déployer InfluxDB avec Docker
* Configurer InfluxDB (org, bucket, token)
* Comprendre la persistance des données (volume Docker)
* Préparer l’intégration avec Node-RED

---

## Contexte

Dans l’architecture actuelle :

```text
PLC → OPC UA → Data Collector → MQTT → Node-RED → InfluxDB
````

👉 Les données sont maintenant :

* collectées ✔
* transportées ✔
* traitées ✔

---

## Problème

Les données ne sont pas encore stockées.

👉 Sans stockage :

❌ pas d’historique
❌ pas d’analyse
❌ pas de monitoring

---

## Solution

👉 Utiliser une base de données adaptée :

👉 **InfluxDB**

---

# Introduction à InfluxDB

---

## Qu’est-ce qu’une base time-series ?

Une base time-series stocke des données avec :

* une valeur
* un timestamp

---

## Exemple

```json id="j4k9zp"
{
  "measurement": "plc1_temperature_motor",
  "value": 45.2,
  "timestamp": 1710000000
}
```

---

## Pourquoi InfluxDB ?

InfluxDB est optimisé pour :

* données IoT
* données temps réel
* monitoring industriel

---

# Partie 1 — Configuration (.env)

---

## Objectif

👉 Configurer automatiquement InfluxDB au démarrage

---

## Création du fichier

```bash id="n1r4lm"
nano .env
```

---

## Contenu

```env id="v9k2pz"
DOCKER_INFLUXDB_INIT_MODE=setup
DOCKER_INFLUXDB_INIT_USERNAME=admin
DOCKER_INFLUXDB_INIT_PASSWORD=admin123
DOCKER_INFLUXDB_INIT_ORG=iiot
DOCKER_INFLUXDB_INIT_BUCKET=edge-GW
INFLUXDB_TOKEN=my-super-token
```

---

## Explication

* username/password → accès interface
* org → organisation logique
* bucket → base de données
* token → sécurité API

---

# Partie 2 — Volume Docker (CRITIQUE)

---

## Objectif

👉 Assurer la persistance des données

---

## Création

```bash id="b3k9qw"
docker volume create influxdb-data
```

---

## Pourquoi c’est important ?

Sans volume :

❌ données perdues
❌ redémarrage = perte totale

Avec volume :

✔ données persistantes
✔ stockage fiable

---

# Partie 3 — Déploiement InfluxDB

---

## Commande

```bash id="u8m2xa"
docker run -d \
  --name influxdb \
  --network iiot-network \
  -p 8086:8086 \
  -v influxdb-data:/var/lib/influxdb2 \
  --env-file .env \
  --restart unless-stopped \
  influxdb:2.7
```

---

## Important

👉 Le conteneur doit être dans :

```text id="3y8rkp"
iiot-network
```

👉 pour permettre la communication avec Node-RED

---

# Partie 4 — Vérification

---

```bash id="d8l4qv"
docker ps
```

---

👉 Le conteneur doit être **Up**

---

# Partie 5 — Accès à l’interface

---

Ouvrir :

```text id="f2m8za"
http://192.168.56.12:8086
```

---

## Connexion

* Username : admin
* Password : admin123
* Organisation : iiot
* Bucket : edge-GW

---

# Partie 6 — Concepts clés

---

## Organisation (Org)

👉 regroupe les ressources du projet

---

## Bucket

👉 base de données contenant les mesures

---

## Token

👉 clé d’accès sécurisée pour écrire/lire

---

## Time-series

👉 données indexées par le temps

---

# Partie 7 — Préparation de l’intégration

---

## Objectif

👉 Préparer Node-RED à envoyer les données

---

## Flux cible

```text id="9x2k7q"
OPC UA → MQTT → Node-RED → InfluxDB
```

---

👉 Node-RED jouera le rôle de :

👉 client d’écriture vers InfluxDB

---

# Analyse

---

## Exercice 1

Pourquoi InfluxDB est adapté à l’IoT ?

---

## Exercice 2

Pourquoi utiliser un volume Docker ?

---

## Exercice 3

Quel est le rôle du bucket edge-GW ?

---

## Exercice 4

Pourquoi utiliser un token ?

---

## Exercice 5 (IMPORTANT)

Pourquoi est-il nécessaire d’avoir un timestamp dans les données ?

---

# Résultat attendu

* InfluxDB lancé
* interface accessible
* configuration fonctionnelle
* volume actif

---

# Hints

---

* vérifier docker ps
* vérifier volume
* vérifier .env
* vérifier logs :

```bash id="v2n8z1"
docker logs influxdb
```

---

# Vision architecture

---

```text id="5p3q8v"
Data → Node-RED → InfluxDB → Stockage
```

---

# Conclusion

InfluxDB permet de :

* stocker les données IoT
* historiser les mesures
* préparer l’analyse

---

👉 C’est une brique essentielle du monitoring industriel.

---

## Prochaine étape

👉 Visualisation avec Grafana

---

