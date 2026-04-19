# Corrigé — TP 07 InfluxDB : Stockage des données IoT (Node-RED → Database)

---

## Compréhension globale

Dans ce TP, nous avons ajouté la couche de stockage à notre architecture IoT.

👉 InfluxDB permet de :

* stocker les données dans le temps
* historiser les mesures
* préparer l’analyse et la visualisation

---

## Position dans l’architecture

```text
PLC → OPC UA → Data Collector → MQTT → Node-RED → InfluxDB
````

👉 InfluxDB est la base de données finale.

---

# Étape 1 — Configuration (.env)

---

## Fichier

```bash id="w2m8d1"
nano .env
```

---

## Contenu

```env id="n8k3pz"
DOCKER_INFLUXDB_INIT_MODE=setup
DOCKER_INFLUXDB_INIT_USERNAME=admin
DOCKER_INFLUXDB_INIT_PASSWORD=admin123
DOCKER_INFLUXDB_INIT_ORG=iiot
DOCKER_INFLUXDB_INIT_BUCKET=edge-GW
INFLUXDB_TOKEN=my-super-token
```

---

## Explication

* INIT_MODE=setup → initialise automatiquement InfluxDB
* USERNAME / PASSWORD → accès interface
* ORG → organisation du projet
* BUCKET → base de données
* TOKEN → clé API pour écrire des données

---

# Étape 2 — Volume Docker (CRITIQUE)

---

## Commande

```bash id="q7v4mz"
docker volume create influxdb-data
```

---

## Pourquoi ?

Sans volume :

❌ données perdues à chaque redémarrage

Avec volume :

✔ données persistantes
✔ stockage fiable

---

## Vérification

```bash id="p4k9nx"
docker volume ls
```

---

# Étape 3 — Déploiement InfluxDB

---

## Commande

```bash id="z3x8f1"
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

## Explication

* --network → connexion au réseau Docker
* -p 8086 → interface web
* -v → persistance des données
* --env-file → configuration automatique

---

## Point critique

👉 InfluxDB doit être dans :

```text id="z7l9kp"
iiot-network
```

👉 pour permettre la communication avec Node-RED

---

# Étape 4 — Vérification

---

```bash id="m8v2t1"
docker ps
```

---

👉 Le conteneur doit être **Up**

---

# Étape 5 — Accès interface

---

Ouvrir :

```text id="b6y2kp"
http://192.168.56.12:8086
```

---

## Connexion

* Username : admin
* Password : admin123
* Organisation : iiot
* Bucket : edge-GW

---

# Étape 6 — Concepts clés (IMPORTANT)

---

## 1. Organisation (Org)

👉 structure logique du projet

---

## 2. Bucket

👉 base de données contenant les mesures

Exemple :

```text id="a9c3r7"
edge-GW
```

---

## 3. Token

👉 clé de sécurité

Permet :

* écrire dans la base
* lire les données

---

## 4. Time-series

👉 données indexées dans le temps

Exemple :

```json id="t7k4pz"
{
  "measurement": "plc1_temperature_motor",
  "value": 45.2,
  "timestamp": 1710000000
}
```

---

# Réponses aux exercices

---

## Exercice 1 — Pourquoi InfluxDB ?

* optimisé pour données temporelles
* performant en IoT
* stockage efficace
* adapté au monitoring

---

## Exercice 2 — Pourquoi volume Docker ?

👉 permet :

* persistance des données
* éviter perte lors restart
* fiabilité du système

---

## Exercice 3 — Rôle du bucket edge-GW

👉 contient :

* toutes les mesures
* données IoT
* historique

---

## Exercice 4 — Pourquoi un token ?

👉 sécurité :

* authentification API
* contrôle d’accès
* protection des données

---

## Exercice 5 — Pourquoi timestamp ?

👉 essentiel car :

* permet l’historisation
* permet les graphiques
* permet l’analyse temporelle

---

# Problèmes fréquents (IMPORTANT)

---

## 1. InfluxDB inaccessible

Vérifier :

```bash id="p2k8dv"
docker ps
```

👉 conteneur doit être Up

---

## 2. Mauvaise configuration .env

👉 vérifier :

* username
* password
* bucket
* token

---

## 3. Données non persistées

👉 vérifier volume :

```bash id="r3x7mf"
docker volume ls
```

---

## 4. Node-RED ne peut pas écrire

Causes possibles :

* mauvais token
* mauvais bucket
* mauvais org

---

## 5. Problème réseau

```bash id="g8m1zr"
docker network inspect iiot-network
```

👉 influxdb et node-red doivent être présents

---

# Compréhension architecture finale

---

```text id="s9z3lk"
PLC → OPC UA → MQTT → Node-RED → InfluxDB
```

---

👉 InfluxDB stocke les données pour :

* analyse
* visualisation
* monitoring

---

# Conclusion

Dans ce TP, vous avez :

* déployé InfluxDB
* configuré une base IoT
* compris org / bucket / token
* mis en place la persistance

---

👉 Vous avez maintenant une architecture complète côté Edge.

---

## Prochaine étape

👉 Visualisation avec Grafana

---

