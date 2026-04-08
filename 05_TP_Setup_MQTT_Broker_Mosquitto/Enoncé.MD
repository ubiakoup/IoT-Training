# TP 05 - Setup MQTT Broker (Mosquitto)

---

## Objectifs pédagogiques

À la fin de ce TP, vous serez capable de :

* Comprendre MQTT
* Déployer un broker MQTT
* Comprendre les réseaux Docker
* Connecter les services entre eux

---

## Contexte

Dans une architecture IoT moderne :

👉 les services doivent communiquer entre eux

Pour cela, nous utilisons :

👉 un réseau Docker commun

---

# Introduction à MQTT

---

## Modèle

MQTT fonctionne en :

👉 Publish / Subscribe

---

## Fonctionnement

```text
Publisher → Broker → Subscriber
```

---

## Concepts

* Broker → serveur central
* Topic → canal
* Payload → donnée

---

# ⚠️ Partie 0 — Création du réseau Docker (CRITIQUE)

---

## Créer le réseau

```bash
docker network create iiot-network
```

---

## Vérifier

```bash
docker network ls
```

---

👉 Le réseau `iiot-network` doit apparaître.

---

# Partie 1 — Lancer le broker MQTT

---

## Télécharger l’image

```bash
docker pull eclipse-mosquitto
```

---

## Lancer le conteneur

```bash
docker run -d \
  --name mqtt-broker \
  --network iiot-network \
  -p 1883:1883 \
  --restart unless-stopped \
  eclipse-mosquitto
```

---

## Vérifier

```bash
docker ps
```

---

# Partie 2 — Test MQTT

---

## Subscriber

```bash
docker exec -it mqtt-broker mosquitto_sub -t test/topic
```

---

## Publisher

```bash
docker exec -it mqtt-broker mosquitto_pub -t test/topic -m "hello"
```

---

## Résultat

```text
hello
```

---

# Partie 3 — Compréhension réseau Docker

---

## Pourquoi un réseau ?

👉 Permet aux conteneurs de communiquer entre eux

---

## Exemple

Le Data Collector pourra utiliser :

```yaml
broker: mosquitto
```

👉 car Docker résout automatiquement le nom

---

## Sans réseau

❌ communication impossible
❌ erreurs de connexion

---

# Partie 4 — Intégration avec Data Collector

---

Configurer :

```yaml
mqtt:
  broker: mqtt-broker
  port: 1883
```

---

# Analyse

---

## Exercice 1

Pourquoi créer un réseau Docker ?

---

## Exercice 2

Que se passe-t-il sans réseau ?

---

## Exercice 3

Pourquoi utiliser le nom du conteneur comme hostname ?

---

## Exercice 4

Quel est le rôle du broker ?

---

# Résultat attendu

* réseau créé
* broker actif
* communication OK

---

# Hints

* docker network ls
* docker inspect
* vérifier nom conteneur
* vérifier ports

---

# Vision globale

```text
OPC-UA → Data Collector → MQTT (network)
```

---

# Conclusion

Le broker MQTT est maintenant intégré dans un réseau Docker.

👉 Base essentielle pour toute l’architecture.

Prochaine étape :

👉 Node-RED

---
