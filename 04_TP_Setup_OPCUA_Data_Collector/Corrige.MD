# Corrigé — TP 04 : OPC-UA Client & Data Collector (Containerisé)

---

## Compréhension globale

Dans ce TP, nous avons mis en place un composant clé d’une architecture IIoT :

👉 le **Data Collector**

---

## Rôle du Data Collector

Le Data Collector agit comme un **pont entre deux mondes** :

```text
OT (machines) → Data Collector → IT (applications)
````

---

## Fonction principale

* lire les données depuis OPC UA (machines)
* écouter les changements en temps réel
* transformer les données
* publier vers MQTT

---

## Architecture globale

```text id="arch1"
PLC → OPC UA Server → Data Collector → MQTT → Applications
```

---

# Étape 1 — Verification du réseau Docker

```bash id="net1"
docker network ls
```
Resultat
```bash id="net1"

NETWORK ID     NAME           DRIVER    SCOPE
5e55e2845ac8   bridge         bridge    local
5e4a857b4525   host           host      local
ab027a0386a3   iiot-network   bridge    local
19c3c688e5da   none           null      local
vagrant@iot-edge:~$
```
notre Reseau iiot-network est bel et bien présent
---

# Étape 2 — requirements.txt

```text id="req1"
opcua
paho-mqtt
cryptography
PyYAML
```

---

## Explication

| Librairie    | Rôle                  |
| ------------ | --------------------- |
| opcua        | connexion OPC UA      |
| paho-mqtt    | communication MQTT    |
| cryptography | sécurité              |
| PyYAML       | lecture configuration |

---

# Étape 3 — config.yml

```yaml id="cfg1"
opcua:
  url: "opc.tcp://192.168.56.11:4840"

mqtt:
  broker: mqtt-broker
  port: 1883

factory:

  plc1:
    temperature_motor: "ns=2;s=plc1.temperature"
    vibration_motor: "ns=2;s=plc1.vibration"
    motor_current: "ns=2;s=plc1.motor_current"
    motor_speed: "ns=2;s=plc1.motor_speed"
    bearing_health: "ns=2;s=plc1.bearing_health"
    time: "ns=2;s=plc1.time"
    ...
    ...
```

---

## ⚠️ Important

👉 L’explication détaillée de ce fichier est disponible dans :

```text id="refcfg"
config.md
```

---

# Étape 4 — data_collector.py

---

## Code

```python id="code1"
(import code identique fourni dans le TP)
```

---

## ⚠️ Important

👉 L’explication complète du fonctionnement du Data Collector est disponible dans :

```text id="refdc"
data_collector.md
```

---

# Étape 5 — Dockerfile

```dockerfile id="dock1"
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY data_collector.py .
COPY config.yml .

CMD ["python", "data_collector.py"]
```

# Étape 6 — Build

```bash id="build1"
docker build -t data-collector .
```

---

# Étape 7 — Lancer le Data Collector

```bash id="run1"
docker run -d \
  --name data-collector \
  --network iiot-network \
  data-collector
```

---

# Étape 9 — Vérification

```bash id="logs1"
docker logs data-collector
```

---

## Résultat attendu

```text id="res1"
Connected to OPC UA Server
Connected to MQTT broker
Subscribed: plc1/temperature_motor
Published -> factory/plc1/temperature_motor: 45.2
```

---

# Analyse

---

## Exercice 1

👉 Le Data Collector fait le lien entre OPC UA (OT) et MQTT (IT)

---

## Exercice 2

👉 config.yml permet de séparer la configuration du code

---

## Exercice 3

👉 MQTT est un protocole léger adapté à l’IoT

---

# Points clés

* architecture event-driven (subscription OPC UA)
* communication temps réel
* découplage OT / IT
* utilisation de Docker

---

# Conclusion

👉 Ce TP met en place un **Data Collector industriel réel**

---

## Vision finale

```text id="finalarch"
PLC → OPC UA → Data Collector → MQTT → Applications
```

---

