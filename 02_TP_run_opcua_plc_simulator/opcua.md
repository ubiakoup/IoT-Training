# OPC UA — Fonctionnement, Architecture et NodeIds (Guide industriel)

---

## Introduction

OPC UA (Open Platform Communications Unified Architecture) est un protocole industriel permettant de connecter :

- machines (PLC)
- capteurs
- systèmes IT (applications, cloud)

👉 Il sert de pont entre le monde **OT (machines)** et **IT (logiciels)**.

---

# 1. Architecture OPC UA

OPC UA fonctionne avec deux éléments principaux :

```

Client OPC UA  ⇄  Serveur OPC UA

```

- Le **serveur** expose les données (machines)
- Le **client** lit ces données

---

# 2. Structure des données (Address Space)

Dans OPC UA, les données sont organisées sous forme d’arbre :

👉 appelé **Address Space**

---

## Exemple industriel

```

Factory
└── PLC1
├── Temperature
├── Pressure
└── MotorSpeed

```

---

## ⚠️ Important

👉 **PLC1 est un Node de type Object (objet)**  
👉 **Temperature, Pressure, MotorSpeed sont des sous-nodes**

Donc :

- PLC1 = machine (niveau haut)
- Temperature = variable (niveau bas)

---

## Interprétation

| Élément | Type | Rôle |
|--------|------|-----|
| PLC1 | Object Node | représente une machine |
| Temperature | Variable Node | représente une donnée |
| Pressure | Variable Node | donnée |
| MotorSpeed | Variable Node | donnée |

👉 PLC1 est un node parent  
👉 les capteurs sont des nodes enfants

---

# 3. Les Nodes

Un **Node** peut représenter :

- une machine (Object)
- une donnée (Variable)
- une fonction (Method)

👉 Dans ce projet :
➡️ on manipule principalement des **Variable Nodes**

---

# 4. NodeId — Identifiant unique

Chaque Node possède un identifiant unique :

👉 **NodeId**

---

## Format

```

ns=<namespace>;type=value

```

---

## Exemple

```

ns=2;s=plc1.temperature

```

---

| Partie | Signification |
|--------|-------------|
| ns=2 | namespace |
| s | type d’identifiant |
| plc1.temperature | identifiant |

---

# 5. Types de NodeId

---

## 🔹 Numeric (i)

```

ns=2;i=5

```

- rapide  
- utilisé en interne  

---

## 🔹 String (s)

```

ns=2;s=plc1.temperature

```

- lisible  
- compréhensible  

---

## 🔹 GUID (g)

```

ns=2;g=UUID

```

- identifiant global unique  

---

## 🔹 ByteString (b)

cas spécifiques

---

# 6. ⚠️ Choix IMPORTANT : s vs i

---

## 🔹 Numeric (i)

### Avantages

- rapide  
- performant  

### Inconvénients

- non lisible  
- difficile à maintenir  

---

## 🔹 String (s)

### Avantages

- lisible  
- stable  
- facile à comprendre  

---

## 🔥 Pourquoi utiliser "s" dans cette architecture

Parce que cette architecture est :

```

OPC UA → MQTT → Node-RED → Grafana

```

👉 Il est essentiel d’avoir une correspondance claire entre les données.

---

## Exemple réel

OPC UA :

```

ns=2;s=plc1.temperature

```

MQTT :

```

factory/plc1/temperature_motor

```

---

👉 Correspondance logique :

| OPC UA | MQTT |
|--------|------|
| plc1.temperature | factory/plc1/temperature |

---

## ⚠️ Problème avec i

```

ns=2;i=5

```

👉 Impossible de comprendre à quoi correspond la donnée  
👉 difficile à mapper avec MQTT  

---

# 7. Résumé des NodeIds

| Type | Usage |
|------|------|
| i | performance interne |
| s | lisibilité / IIoT |
| g | systèmes distribués |
| b | cas spécifiques |

---

# 8. Communication réseau (OSI)

---

## Couches utilisées

| Couche | Rôle |
|-------|-----|
| Application | OPC UA |
| Transport | TCP |
| Réseau | IP |
| Physique | Ethernet |

---

## Schéma

```

OPC UA → TCP → IP → Ethernet

```

---

👉 OPC UA fonctionne sur TCP  
👉 port standard : **4840**

---

# 9. Fonctionnement global

1. le serveur expose les nodes  
2. le client se connecte  
3. il lit les NodeIds  
4. il récupère les valeurs  

---

## Flux réel

```

PLC → OPC UA Server → Client → MQTT → Dashboard

```

---

# 10. Conclusion

OPC UA est :

- moderne  
- sécurisé  
- adapté à l’IoT industriel  

---

👉 À retenir :

- PLC = Object Node  
- capteurs = Variable Nodes  
- chaque Node a un NodeId  
- privilégier **s (string)** dans les architectures IIoT  

---

