# TP 03 — MQTT & Mise en place du premier service sur l’Edge (Réseau Docker + Broker Mosquitto)

---

## Objectifs pédagogiques

À la fin de ce TP, vous serez capable de :

* Comprendre le protocole MQTT
* Comprendre la différence entre MQTT et HTTP
* Comprendre le modèle Publish / Subscribe
* Comprendre le rôle du broker
* Comprendre le rôle du réseau Docker
* Déployer un premier service sur l’Edge (MQTT)

---

## Contexte

Dans une architecture IoT industrielle, l’Edge Gateway exécute plusieurs services :

* collecte de données
* traitement
* communication

👉 Ces services doivent communiquer entre eux.

👉 Pour cela, nous utilisons :

👉 **un réseau Docker**

---

# Partie 1 — MQTT dans le modèle OSI

---

MQTT est un protocole de la couche applicative (Layer 7).

Il repose sur :

```text
MQTT → TCP → IP
````

👉 Même base que HTTP, mais logique différente.

---

# Partie 2 — MQTT vs HTTP

---

## HTTP

```text
Client → Requête → Serveur → Réponse
```

* communication synchrone
* nécessite plusieurs requêtes

---

## MQTT

```text
Publisher → Broker → Subscriber
```

* communication asynchrone
* temps réel
* découplée

---

## Comparaison

| Critère       | MQTT                | HTTP               |
| ------------- | ------------------- | ------------------ |
| Modèle        | Publish / Subscribe | Request / Response |
| Communication | Asynchrone          | Synchrone          |
| Overhead      | Faible              | Élevé              |

---

# Partie 3 — Fonctionnement de MQTT

---

## Rôles

### Publisher

👉 envoie des données

---

### Broker

👉 serveur central (ex : Mosquitto)

---

### Subscriber

👉 reçoit les données

---

## Concepts clés

### Topic

```text
factory/plc1/temperature
```

---

### Payload

```json
{
  "value": 45.2
}
```

---

# Partie 4 — Réseau Docker (CRITIQUE)

---

## Pourquoi un réseau ?

Dans Docker, les conteneurs sont isolés.

👉 Sans réseau commun :

❌ pas de communication
❌ erreurs de connexion
❌ impossible de construire une architecture

---

## Objectif

👉 créer un réseau qui permettra :

* aux services de communiquer
* d’utiliser des noms au lieu des IP
* de construire une architecture IoT

---

## Création du réseau

```bash
docker network create iiot-network
```

---

## Vérification

```bash
docker network ls
```

---

👉 Le réseau `iiot-network` doit apparaître.

---

## Compréhension

Dans ce réseau :

👉 chaque conteneur peut être joint par son nom

Exemple :

```text
mqtt-broker
```

👉 devient une adresse réseau

---

# Partie 5 — Déploiement du premier service (MQTT)

---

## Objectif

👉 Déployer le premier service de l’Edge :

👉 le broker MQTT

---

## Consigne

Lancer un conteneur Mosquitto avec :

* nom : mqtt-broker
* réseau : iiot-network
* port : 1883

---

## À faire

👉 Écrire la commande Docker permettant de lancer ce service

---

# Partie 6 — Validation

---

## Vérifier le conteneur

```bash
docker ps
```

---

👉 Le conteneur doit être en état **Up**

---

## Test (optionnel)

Subscriber :

```bash
docker exec -it mqtt-broker mosquitto_sub -t test/topic
```

Publisher :

```bash
docker exec -it mqtt-broker mosquitto_pub -t test/topic -m "hello"
```

---

## Résultat attendu

```text
hello
```

---

# Analyse

---

## Question 1

Quelle est la différence entre MQTT et HTTP ?

---

## Question 2

Pourquoi MQTT est adapté à l’IoT ?

---

## Question 3

Quel est le rôle du broker ?

---

## Question 4

Pourquoi créer un réseau Docker ?

---

## Question 5

Pourquoi utiliser le nom du conteneur comme hostname ?

---

# Vision architecture

---

```text
Edge → Réseau Docker → MQTT Broker
```

---

# Conclusion

Dans ce TP, vous avez :

* compris MQTT
* compris son fonctionnement
* compris le rôle du réseau Docker
* déployé le premier service de l’Edge

👉 Cette base est essentielle pour la suite :

➡️ Data Collector (OPC UA → MQTT)

