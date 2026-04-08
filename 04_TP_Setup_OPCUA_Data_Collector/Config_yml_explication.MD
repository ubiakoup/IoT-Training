# Configuration du Data Collector — config.yml

---

## Introduction

Le fichier `config.yml` est un élément central du système.

Il permet de :

* configurer la connexion OPC-UA
* configurer le broker MQTT
* définir les capteurs à collecter

👉 C’est le fichier que l’ingénieur doit adapter en fonction de l’environnement industriel.

---

## Structure globale

Le fichier est structuré en trois parties :

```yaml
opcua:
mqtt:
factory:
```

---

# 1. Configuration OPC-UA

```yaml
opcua:
  url: "opc.tcp://192.168.0.141:4840"
```

---

## Explication

* `opc.tcp://` → protocole OPC-UA
* `192.168.0.141` → adresse du serveur OPC-UA
* `4840` → port standard OPC-UA

---

## Important

👉 Cette adresse doit correspondre à :

* la machine où tourne le simulateur
* ou un automate réel

---

# 2. Configuration MQTT

```yaml
mqtt:
  broker: mosquitto
  port: 1883
```

---

## Explication

* `broker` → adresse du serveur MQTT
* `port` → port MQTT (1883 par défaut)

---

## Cas possibles

### En local (Docker)

```yaml
broker: mosquitto
```

👉 nom du conteneur Docker

---

### En réseau

```yaml
broker: 192.168.0.50
```

👉 IP du serveur MQTT

---

# 3. Configuration des capteurs (factory)

---

## Structure

```yaml
factory:
  plc1:
  plc2:
  plc3:
```

---

👉 Chaque PLC représente un système industriel

---

# PLC1 — Motor System

```yaml
plc1:
  temperature_motor: "ns=2;s=plc1.temperature"
  vibration_motor: "ns=2;s=plc1.vibration"
  motor_current: "ns=2;s=plc1.motor_current"
  motor_speed: "ns=2;s=plc1.motor_speed"
  bearing_health: "ns=2;s=plc1.bearing_health"
  time: "ns=2;s=plc1.time"
```

---

## Explication

| Tag               | Description        |
| ----------------- | ------------------ |
| temperature_motor | Température moteur |
| vibration_motor   | Vibration          |
| motor_current     | Courant moteur     |
| motor_speed       | Vitesse            |
| bearing_health    | Santé du roulement |
| time              | Timestamp          |

---

# PLC2 — Hydraulic System

```yaml
plc2:
  hydraulic_pressure: "ns=2;s=plc2.pressure"
  hydraulic_temp: "ns=2;s=plc2.temperature"
  flow_rate: "ns=2;s=plc2.flow_rate"
  oil_level: "ns=2;s=plc2.oil_level"
  time: "ns=2;s=plc2.time"
```

---

# PLC3 — Energy Monitoring

```yaml
plc3:
  voltage: "ns=2;s=plc3.voltage"
  current: "ns=2;s=plc3.current"
  energy: "ns=2;s=plc3.energy"
  power_factor: "ns=2;s=plc3.power_factor"
  time: "ns=2;s=plc3.time"
```

---

# Comprendre les NodeID OPC-UA

---

## Exemple

```text
ns=2;s=plc1.temperature
```

---

## Décomposition

| Élément          | Signification     |
| ---------------- | ----------------- |
| ns=2             | namespace         |
| s=               | string identifier |
| plc1.temperature | nom du capteur    |

---

## Important

👉 Ces NodeID doivent correspondre exactement :

* au serveur OPC-UA
* sinon aucune donnée ne sera récupérée

---

# Fonctionnement global

Le Data Collector :

1. lit le fichier config.yml
2. se connecte à OPC-UA
3. récupère les NodeID
4. s’abonne aux données
5. publie vers MQTT

---

# Exemple de mapping MQTT

```text
factory/plc1/temperature_motor → 45.2
```

---

# Bonnes pratiques

* ne jamais hardcoder les NodeID dans le code
* toujours utiliser config.yml
* documenter chaque capteur
* vérifier les NodeID avec UAExpert

---

# Problèmes fréquents

---

## 1. Aucun message MQTT

Cause :

* NodeID incorrect

---

## 2. OPC-UA connecté mais pas de données

Cause :

* mismatch entre config.yml et serveur

---

## 3. Mauvais broker MQTT

Cause :

* mauvais hostname

---

# Conclusion

Le fichier `config.yml` est :

👉 le point de configuration principal du système

C’est ici que l’on connecte :

* le monde industriel
* le pipeline IoT

---
