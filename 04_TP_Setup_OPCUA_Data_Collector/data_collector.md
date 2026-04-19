# 📡 OPC UA → MQTT Data Collector (Explication Complète)

---

#  1. Objectif du programme

Ce script sert à :

```text
Lire des données industrielles (OPC UA)
→ Les transformer en JSON
→ Les envoyer vers MQTT
```

👉 Concrètement :

```text
Machine (PLC) → OPC UA → Python → MQTT → Cloud
```

---

# 🧱 2. Les imports (les briques du programme)

```python
import yaml
import time
import json
import logging
from opcua import Client
from opcua import ua
import paho.mqtt.client as mqtt
```

---

## 🔍 Explication simple

| Module         | Rôle                                   |
| -------------- | -------------------------------------- |
| `yaml`         | Lire le fichier config.yml             |
| `time`         | gérer le temps (timestamp, pause)      |
| `json`         | transformer les données en format JSON |
| `logging`      | afficher des logs propres              |
| `opcua.Client` | se connecter au serveur OPC UA         |
| `mqtt`         | envoyer les données via MQTT           |

---

# 🪵 3. Configuration des logs

```python
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
```

👉 Ça permet d’avoir des logs lisibles :

```text
2026-04-19 12:00:00 | INFO | Connected to MQTT broker
```

---

# ⚙️ 4. Lecture du fichier config.yml

```python
with open("config.yml") as f:
    config = yaml.safe_load(f)
```

👉 On charge la configuration externe

---

## 📦 Exemple de config

```yaml
opcua:
  url: opc.tcp://192.168.0.141:4840

mqtt:
  broker: mosquitto
  port: 1883
```

---

## 🔍 Extraction

```python
opc_url = config["opcua"]["url"]
mqtt_broker = config["mqtt"]["broker"]
mqtt_port = config["mqtt"]["port"]
```

👉 On récupère les infos nécessaires

---

# 📡 5. Connexion MQTT (avec retry)

```python
def connect_mqtt():
```

---

##  Pourquoi une boucle ?

```python
while True:
```

👉 Parce que :

❌ Le broker peut être down
❌ Le réseau peut couper

👉 Donc on retry jusqu’à succès

---

##  Connexion

```python
client.connect(mqtt_broker, mqtt_port)
```

---

##  Logs

```python
logging.info("Connected to MQTT broker")
```

---

##  Retry en cas d’erreur

```python
time.sleep(5)
```

👉 attend 5 secondes avant de réessayer

---

##  Démarrage MQTT

```python
mqtt_client.loop_start()
```

👉 Lance un thread en arrière-plan pour gérer MQTT

---

# 🏭 6. Connexion OPC UA

Même logique que MQTT :

```python
def connect_opcua():
```

---

## 🔁 Retry automatique

```python
while True:
```

👉 ultra important en industrie

---

##  Connexion

```python
client = Client(opc_url)
client.connect()
```

---

#  7. Chargement des nodes OPC UA

```python
nodes = {}
```

👉 structure finale :

```text
nodes = {
  plc1: {
    temperature_motor: Node,
    vibration_motor: Node
  }
}
```

---

## 🔄 Boucle

```python
for plc, tags in config["factory"].items():
```

👉 on parcourt tous les PLC

---

## 🔍 Récupération des nodes

```python
node = opc_client.get_node(nodeid)
```

👉 transforme un string en objet OPC UA

---

# 📢 8. Le cœur du système (Subscription)

---

## 🧠 Classe handler

```python
class SubHandler:
```

👉 appelée automatiquement quand une valeur change

---

## ⚡ Fonction principale

```python
def datachange_notification(self, node, val, data):
```

👉 se déclenche à chaque changement

---

# 🔍 9. Identifier le node

```python
nodeid = node.nodeid.to_string()
```

👉 permet de savoir quel capteur a changé

---

## 🔄 Matching PLC + tag

```python
for plc, tags in nodes.items():
```

👉 on cherche à quel PLC appartient ce node

---

# 📡 10. Création du message MQTT

---

## 🏷 Topic

```python
topic = f"factory/{plc}/{tag}"
```

👉 exemple :

```text
factory/plc1/temperature_motor
```

---

##  Payload

```python
payload = {
    "plc": plc,
    "tag": tag,
    "value": val,
    "timestamp": time.time()
}
```

---

👉 Résultat :

```json
{
  "plc": "plc1",
  "tag": "temperature_motor",
  "value": 56.2,
  "timestamp": 1713120000
}
```

---

#  11. Envoi MQTT

```python
mqtt_client.publish(topic, json.dumps(payload))
```

👉 envoie les données vers le broker

---

#  12. Création de la subscription OPC UA

```python
subscription = opc_client.create_subscription(500, handler)
```

---

##  Explication

* `500` = 500 ms (fréquence)
* `handler` = qui traite les données

---

##  Abonnement aux nodes

```python
subscription.subscribe_data_change(node)
```

👉 déclenche des événements automatiques

---

#  13. Boucle principale

```python
while True:
    time.sleep(1)
```

👉 garde le programme vivant

---

#  14. Gestion des erreurs

```python
except Exception as e:
```

---

##  Reconnexion OPC UA

```python
opc_client = connect_opcua()
```

👉 auto-healing system 💪

---

#  15. Résumé global

---

##  Flux complet

```text
1. Connexion MQTT
2. Connexion OPC UA
3. Chargement des nodes
4. Subscription OPC UA
5. Changement valeur détecté
6. Création message JSON
7. Envoi vers MQTT
```

---

## Ce que fait ton code

✔ temps réel
✔ automatique
✔ robuste (retry)
✔ scalable

---

#  16. Points forts (niveau pro)

---

✔ Retry automatique
✔ Logging propre
✔ Config externalisée
✔ Event-driven (subscription)

---

#  17. Améliorations possibles

---

### 🔹 1. Ajouter QoS MQTT

```python
mqtt_client.publish(topic, payload, qos=1)
```

---

### 🔹 2. Ajouter buffer en cas de perte réseau

---

### 🔹 3. Ajouter reconnection MQTT

---

### 🔹 4. Ajouter filtre (ne pas envoyer si pas de changement significatif)

---

# ✅ Conclusion

Ce script est :

👉 un **edge data collector industriel**
👉 équivalent à une gateway IoT

---

##  Niveau réel

✔ DevOps IoT
✔ Industrial IoT Engineer
✔ Edge Computing

---
