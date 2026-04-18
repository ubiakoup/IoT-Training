# TP 08 - Envoi des données Node-RED vers InfluxDB

---

## Objectifs pédagogiques

* Envoyer des données vers InfluxDB
* Comprendre le format time-series
* Vérifier le stockage des données

---

## Contexte

Nous avons :

* MQTT (transport)
* Node-RED (processing)
* InfluxDB (stockage)

👉 Il faut maintenant connecter Node-RED à InfluxDB

---

# Partie 1 — Installer le node InfluxDB

Dans Node-RED :

* Menu → Manage Palette
* Installer :
  👉 node-red-contrib-influxdb

---

# Partie 2 — Création du flow

---

## Étape 1 — MQTT IN

Topic :

```text id="l1x2a3"
factory/+/+
```

---

## Étape 2 — Function

```javascript id="m4n5o6"
msg.payload = {
    measurement: "factory_data",
    fields: {
        value: parseFloat(msg.payload)
    },
    tags: {
        topic: msg.topic
    },
    timestamp: new Date()
};
return msg;
```

---

## Étape 3 — InfluxDB OUT

Configurer :

* URL : http://influxdb:8086
* Org : iiot
* Bucket : edge-GW
* Token : my-super-token

---

## Flow final

```text id="p7q8r9"
MQTT → Function → InfluxDB
```

---

# Partie 3 — Vérification

---

Ouvrir :

```text id="s1t2u3"
http://localhost:8086
```

---

## Aller dans Data Explorer

👉 vérifier que les données arrivent

---

# Résultat attendu

* données visibles dans InfluxDB
* pipeline fonctionnel

---

# Conclusion

Node-RED alimente maintenant InfluxDB.

---

## Prochaine étape

👉 Visualisation avec Grafana

---
