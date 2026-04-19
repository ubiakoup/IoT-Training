# ✅ CORRIGÉ.MD FINAL — UN SEUL BLOC COPIABLE

````md
# Corrigé — TP 03 MQTT : Réseau Docker & Déploiement du Broker Mosquitto

---

## Compréhension globale

Dans ce TP, nous avons introduit deux éléments fondamentaux d’une architecture IoT :

👉 le protocole MQTT  
👉 le réseau Docker  

Ces deux briques permettent de construire une communication fiable entre services.

---

# MQTT dans le modèle OSI

MQTT est un protocole de la couche applicative (Layer 7).

Il repose sur :

```text
MQTT → TCP → IP
````

👉 Comme HTTP, mais avec une logique différente.

---

# Différence entre MQTT et HTTP

### HTTP

```text
Client → Requête → Serveur → Réponse
```

* communication synchrone
* nécessite plusieurs requêtes

---

### MQTT

```text
Publisher → Broker → Subscriber
```

* communication asynchrone
* temps réel
* découplée

---

👉 MQTT est donc mieux adapté aux architectures IoT.

---

# Fonctionnement de MQTT

## Les rôles

### Publisher

👉 envoie des données

Exemples :

* capteurs
* PLC
* Data Collector

---

### Broker

👉 serveur central

Il :

* reçoit les messages
* les redistribue

👉 Exemple : Mosquitto

---

### Subscriber

👉 reçoit les données

Exemples :

* Node-RED
* Grafana

---

## Concepts clés

### Topic

Canal de communication :

```text
factory/plc1/temperature
```

---

### Payload

Donnée envoyée :

```json
{
  "value": 45.2
}
```

---

# Réponses aux questions

---

## Question 1 — Différence MQTT vs HTTP

MQTT utilise un modèle Publish / Subscribe (asynchrone).
HTTP utilise un modèle Request / Response (synchrone).

---

## Question 2 — Pourquoi MQTT est adapté à l’IoT ?

* faible consommation réseau
* communication temps réel
* connexion persistante
* léger

---

## Question 3 — Rôle du broker

Le broker :

* reçoit les messages
* distribue les messages aux abonnés

👉 c’est le cœur du système MQTT

---

## Question 4 — Pourquoi créer un réseau Docker ?

Dans Docker, les conteneurs sont isolés.

Sans réseau :

❌ ils ne peuvent pas communiquer
❌ les connexions échouent

👉 Le réseau permet :

✔ communication entre services
✔ résolution DNS interne
✔ architecture distribuée

---

## Question 5 — Pourquoi utiliser le nom du conteneur ?

Dans un réseau Docker :

👉 le nom du conteneur devient une adresse réseau

Exemple :

```text
mqtt-broker
```

👉 utilisé par les autres services comme hostname

---

# Réseau Docker (Partie critique)

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

## Fonctionnement

Dans ce réseau :

👉 chaque conteneur peut communiquer avec les autres
👉 via leur nom (DNS interne Docker)

---

# Déploiement du broker MQTT

---

## Commande

```bash
docker run -d \
  --name mqtt-broker \
  --network iiot-network \
  -p 1883:1883 \
  eclipse-mosquitto
```

---

## Explication

* docker run → lance un conteneur
* -d → mode détaché
* --name → nom du conteneur
* --network → connexion au réseau Docker
* -p 1883:1883 → port MQTT
* eclipse-mosquitto → image officielle

---

# Vérification

```bash
docker ps
```

---

👉 Le conteneur doit être en état **Up**

---

# Test du broker (optionnel)

Subscriber :

```bash
docker exec -it mqtt-broker mosquitto_sub -t test/topic
```

Publisher :

```bash
docker exec -it mqtt-broker mosquitto_pub -t test/topic -m "hello"
```

---

Résultat :

```text
hello
```

---

# Compréhension architecture

Dans notre projet :

```text
OPC UA → Data Collector → MQTT → Applications
```

👉 MQTT est le point central de communication.

---

# Point important pour la suite

Dans le prochain TP, le Data Collector utilisera :

```yaml
mqtt:
  broker: mqtt-broker
  port: 1883
```

👉 Cela fonctionne uniquement si :

✔ même réseau Docker
✔ broker déjà lancé

---

# Conclusion

Dans ce TP, vous avez :

* compris MQTT
* compris le rôle du broker
* compris le modèle Publish / Subscribe
* compris le rôle du réseau Docker
* déployé votre premier service sur l’Edge

---

👉 Le réseau Docker est indispensable pour toute architecture distribuée.

👉 MQTT est la brique centrale de communication.

---

Prochaine étape :

👉 connecter le Data Collector (OPC UA → MQTT)

---

