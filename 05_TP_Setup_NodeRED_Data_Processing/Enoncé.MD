# TP 06 — Node-RED : Traitement des données IoT (MQTT → Processing)

---

## Objectifs pédagogiques

À la fin de ce TP, vous serez capable de :

* Comprendre le rôle de Node-RED dans une architecture IoT
* Déployer Node-RED avec Docker
* Se connecter à MQTT
* Créer un flow de traitement
* Manipuler des données industrielles
* Écrire une logique dans un node Function

---

## Contexte

Dans l’architecture actuelle :

```text
OPC UA → Data Collector → MQTT
````

👉 Les données arrivent sous forme de messages JSON.

Exemple :

```json
{
  "plc": "plc1",
  "tag": "temperature_motor",
  "value": 45.2,
  "timestamp": 1710000000
}
```

---

## Problème

Ces données :

* ne sont pas encore structurées pour stockage
* ne sont pas filtrées
* contiennent du bruit (timestamps, formats, etc.)

---

## Solution

👉 Utiliser Node-RED pour :

* filtrer
* nettoyer
* transformer
* préparer les données

---

# Partie 1 — Déploiement Node-RED

---

```bash
docker run -d \
  --name node-red \
  --network iiot-network \
  -p 1880:1880 \
  -v node-red-data:/data \
  --restart unless-stopped \
  nodered/node-red
```

---

# Partie 2 — Accès

---

Ouvrir :

```text
http://192.168.56.12:1880
```

---

# Partie 3 — Création du flow

---

## Objectif

Créer le pipeline suivant :

```text
MQTT IN → Function → DEBUG
```

---

## Étape 1 — MQTT IN

Configurer :

* Broker : `mqtt-broker`
* Port : `1883`

---

## Topic

```text
factory/+/+
```

---

👉 Permet de recevoir toutes les données

---

# Partie 4 — Traitement des données (IMPORTANT)

---

## Objectif

👉 Écrire une fonction Node-RED qui :

* lit les données MQTT
* ignore les timestamps inutiles
* extrait :

  * plc
  * tag
  * value
* convertit la valeur en nombre
* prépare un format propre

---

## Consigne

Dans le node **Function**, écrire un script JavaScript qui :

### 1. Parse le message MQTT

* gérer string ou JSON

---

### 2. Extraire les informations

* machine (plc)
* capteur (tag)
* valeur (value)

---

### 3. Nettoyer la donnée

* convertir en nombre
* gérer les erreurs

---

### 4. Ignorer certains messages

👉 ignorer :

```text
tag = time
```

---

### 5. Construire une nouvelle structure

Exemple attendu :

```json
{
  "measurement": "plc1_temperature_motor",
  "value": 45.2,
  "timestamp": 1710000000
}
```

---

## Indice

👉 Vous pouvez utiliser :

```javascript
msg.topic.split("/")
JSON.parse()
Number()
```

---

## Résultat attendu

👉 Dans le debug :

* données propres
* valeurs numériques
* structure cohérente

---

# Partie 5 — Validation

---

## Flow final

```text
MQTT → Function → Debug
```

---

## Résultat

👉 Données transformées en temps réel

---

# Analyse

---

## Exercice 1

Quel est le rôle de Node-RED dans cette architecture ?

---

## Exercice 2

Pourquoi transformer les données avant stockage ?

---

## Exercice 3

Quel est le rôle du node MQTT IN ?

---

## Exercice 4

Pourquoi utiliser un node Function ?

---

## Exercice 5 (IMPORTANT)

Expliquez :

👉 pourquoi il faut convertir les valeurs en **nombre**

---

# Hints

---

* vérifier MQTT
* vérifier topic
* vérifier format JSON
* utiliser console debug Node-RED

---

# Vision architecture

---

```text
PLC → OPC UA → Data Collector → MQTT → Node-RED → Processing
```

---

# Conclusion

Node-RED permet :

* de transformer les données industrielles
* de préparer le stockage
* d’ajouter de la logique métier

---

## Prochaine étape

👉 Stockage avec InfluxDB

---

