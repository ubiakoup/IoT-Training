# Corrigé - TP 08 Grafana

---

## Étape 1 — Volume

```bash id="d3k8f2"
docker volume create grafana-storage
```

---

## Étape 2 — Lancement

```bash id="v8k2p1"
docker run -d \
  --name grafana \
  --network iiot-network \
  -p 3000:3000 \
  -v grafana-storage:/var/lib/grafana \
  grafana/grafana
```

---

## Vérification

```bash id="m2k7p3"
docker ps
```

---

## Accès

```text id="j3k9p1"
http://localhost:3000
```

---

## Connexion

* admin / admin

---

## Étape 3 — Data Source

Configurer :

* URL : http://influxdb:8086
* Org : iiot
* Bucket : edge-GW
* Token : my-super-token

---

## Étape 4 — Dashboard

Créer un panel avec :

```text id="t2k8p3"
from(bucket: "edge-GW")
  |> range(start: -1h)
```

---

## Exercice 1

### Rôle Grafana

* visualisation
* monitoring

---

## Exercice 2

### Pourquoi InfluxDB

* source des données

---

## Exercice 3

### Réseau Docker

* communication interne

---

## Exercice 4

### Dashboard

* visualiser les données

---

## Problèmes fréquents

---

### Data source KO

* vérifier token
* vérifier URL

---

### Pas de données

* vérifier Node-RED
* vérifier InfluxDB

---

### Grafana inaccessible

* vérifier port 3000

---

## Vision globale

```text id="x9k3p2"
InfluxDB → Grafana → Dashboard
```

---

## Conclusion

Grafana est opérationnel.

👉 visualisation complète du système IoT

---

## Prochaine étape

👉 Docker Compose (industrialisation)

---
