# Corrigé - TP 05 MQTT Broker avec réseau Docker

---

## Étape 1 — Création du réseau

```bash
docker network create iiot-network
```

---

## Vérification

```bash
docker network ls
```

---

## Étape 2 — Lancer Mosquitto

```bash
docker run -d \
  --name mqtt-broker \
  --network iiot-network \
  -p 1883:1883 \
  eclipse-mosquitto
```

---

## Vérification

```bash
docker ps
```

---

## Test Subscriber

```bash
docker exec -it mqtt-broker mosquitto_sub -t test/topic
```

---

## Test Publisher

```bash
docker exec -it mqtt-broker mosquitto_pub -t test/topic -m "hello"
```

---

## Résultat

```text
hello
```

---

## Exercice 1

### Pourquoi réseau Docker ?

Permet aux conteneurs de communiquer.

---

## Exercice 2

### Sans réseau

* pas de communication
* erreurs réseau

---

## Exercice 3

### Hostname

Docker permet d’utiliser :

👉 nom du conteneur = DNS interne

---

## Exercice 4

### Broker MQTT

* reçoit
* distribue
* connecte

---

## Problèmes fréquents

---

### Réseau absent

```bash
docker network ls
```

---

### Mauvais réseau

```bash
docker inspect mqtt-broker
```

---

### Pas de communication

* vérifier nom broker
* vérifier port

---

## Conclusion

MQTT est opérationnel dans un réseau Docker.

---

## Vision

```text
Containers → Network → Communication
```

---

## Prochaine étape

👉 Node-RED

---
