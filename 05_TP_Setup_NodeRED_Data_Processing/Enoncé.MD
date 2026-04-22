
# TP 05 — Node-RED : Traitement des données IoT (MQTT → Processing)

---

## 🎯 Objectifs pédagogiques

À la fin de ce TP, vous serez capable de :

- Comprendre le rôle de Node-RED dans une architecture IoT industrielle  
- Déployer Node-RED avec Docker  
- Se connecter à un broker MQTT  
- Créer un flow de traitement de données  
- Manipuler des données industrielles (JSON)  
- Implémenter une logique métier avec un node **Function**  
- Visualiser des données avec Node-RED Dashboard  
- Exporter un flow pour réutilisation (approche DevOps)  

---

## 🧠 Contexte

Dans notre architecture IIoT :

```text
PLC → OPC UA → Data Collector → MQTT
````

👉 Les données sont publiées sur MQTT sous forme de messages JSON.

### Exemple :

```json
{
  "plc": "plc1",
  "tag": "temperature_motor",
  "value": 45.2,
  "timestamp": 1710000000
}
```

---

## ⚠️ Problématique

Les données MQTT sont :

* non structurées pour le stockage
* non filtrées
* bruitées (formats variables, données inutiles)

---

## ✅ Solution

👉 Utiliser **Node-RED** comme couche de traitement :

* Filtrer
* Nettoyer
* Transformer
* Préparer les données pour le stockage (InfluxDB)

---

# 🚀 Partie 1 — Déploiement de Node-RED

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

# 🌐 Partie 2 — Accès à l’interface

Ouvrir dans le navigateur :

```
http://192.168.56.12:1880
```

---

# 🔧 Partie 3 — Création du flow

## 🎯 Objectif

Créer le pipeline suivant :

```text
MQTT IN → Function → Debug
```
---

## 📡 Étape 1 — Configuration MQTT IN

Configurer :

* Broker : `mqtt-broker`
* Port : `1883`

### Topic :

```
factory/+/+
```

👉 Permet de recevoir toutes les données des PLC.

---

# 🧠 Partie 4 — Traitement des données (IMPORTANT)

## 🎯 Objectif

Créer une fonction Node-RED qui :

* Lit les données MQTT
* Extrait les informations utiles
* Nettoie les données
* Convertit les valeurs
* Génère un format prêt pour le stockage

---

## 🧪 Travail demandé

Dans le node **Function**, implémenter :

### 1. Parsing du message

* Gérer :

  * JSON
  * string

---

### 2. Extraction des champs

* `plc`
* `tag`
* `value`

---

### 3. Nettoyage

* Conversion en nombre
* Gestion des erreurs

---

### 4. Filtrage

Ignorer :

```
tag = time
```

---

### 5. Transformation

Construire :

```json
{
  "measurement": "plc1_temperature_motor",
  "value": 45.2,
  "timestamp": 1710000000
}
```

---

## 💡 Indices

```javascript
msg.topic.split("/")
JSON.parse()
Number()
```

---

## ✅ Résultat attendu

Dans Debug :

* données propres
* valeurs numériques
* structure cohérente

---

# 🧪 Partie 5 — Validation

## Flow final

```text
MQTT → Function → Debug
```

---

## Résultat

👉 Données transformées en temps réel.

---

# 📊 Partie 6 — Visualisation avec Node-RED Dashboard

## 🎯 Objectif

Afficher les données industrielles en temps réel.

---

## 🧩 Installation (via interface graphique)

👉 Ne PAS utiliser le terminal.

### Étapes :

1. Ouvrir Node-RED
2. Menu (☰)
3. **Manage Palette**
4. Onglet **Install**
5. Rechercher :

```
@flowfuse/node-red-dashboard
```

6. Cliquer sur **Install**

---

## 🏗️ Organisation du Dashboard

👉 Bonne pratique :

➡️ **1 page = 1 système industriel**

---

### Structure recommandée :

* 🔵 PLC1 — Motor System
* 🟢 PLC2 — Hydraulic System
* 🟡 PLC3 — Energy System

---

## 🌐 Accès

```
http://192.168.56.12:1880/dashboard
```

---

## 🧪 Bonnes pratiques

* Nommer clairement les widgets
* Ajouter les unités (°C, bar, kW…)
* Séparer les systèmes
* Éviter les dashboards surchargés

---

# 📦 Partie 7 — Export du Flow (IMPORTANT)

## 🎯 Objectif

Sauvegarder et versionner votre travail.

---

## 📤 Étapes

1. Menu (☰)
2. **Export**
3. Sélectioner **all flows**
4. cliquer sur Download

---

## 📁 Stockage recommandé

```
project-iot/
 └── flows/
      └── flows.json
```

---

## 🎯 Résultat attendu

* Flow complet exporté
* Réutilisable
* Versionnable (Git)

---

# 🧠 Analyse & Questions

## ❓ Exercice 1

Quel est le rôle de Node-RED dans cette architecture ?

---

## ❓ Exercice 2

Pourquoi transformer les données avant stockage ?

---

## ❓ Exercice 3

Quel est le rôle du node MQTT IN ?

---

## ❓ Exercice 4

Pourquoi utiliser un node Function ?

---

## ❓ Exercice 5 (IMPORTANT)

Pourquoi faut-il convertir les valeurs en **nombre** ?

---

# 🧩 Hints

* Vérifier MQTT
* Vérifier le topic
* Vérifier JSON
* Utiliser Debug
* Observer `msg.payload`

---

# 🏗️ Vision globale

```text
PLC → OPC UA → Data Collector → MQTT → Node-RED → Processing → Stockage
```

---

# 🏁 Conclusion

Node-RED permet :

* Transformation des données industrielles
* Préparation au stockage
* Implémentation de logique métier
* Visualisation temps réel

---

## 🔜 Prochaine étape

👉 Intégration avec **InfluxDB** + **Grafana**

---
