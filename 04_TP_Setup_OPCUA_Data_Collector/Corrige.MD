# Corrigé - TP 04 Data Collector Containerisé

---

## Compréhension globale

Le Data Collector permet de :

* lire les données OPC-UA
* les envoyer vers MQTT

Il est exécuté dans un conteneur Docker.

---

## Validation

---

### Build

```bash
docker build -t data-collector .
```

---

### Run

```bash
docker run -d --name data-collector data-collector
```

---

### Logs

```bash
docker logs data-collector
```

---

## Exercice 1

### Rôle du Data Collector

* récupérer les données OT
* les envoyer vers IT

---

## Exercice 2

### Pourquoi Docker ?

* portabilité
* isolation
* déploiement rapide

---

## Exercice 3

### Rôle Dockerfile

* définir environnement
* installer dépendances
* lancer application

---

## Exercice 4

### OPC-UA + MQTT

* OPC-UA → industriel
* MQTT → IoT

---

## Problèmes courants

---

### Pas de connexion OPC-UA

* vérifier IP
* vérifier port

---

### MQTT KO

* vérifier broker
* vérifier port

---

### Pas de logs

```bash
docker logs data-collector
```

---

### Conteneur arrêté

```bash
docker ps -a
```

---

## Conclusion

Le pipeline OT → Edge → MQTT est opérationnel.

---

## Vision

```text
OPC-UA → Docker → MQTT
```

---

## Prochaine étape

👉 Mosquitto (MQTT Broker)

---
