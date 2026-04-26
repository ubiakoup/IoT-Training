# TP13 – Corrigé : Event-Driven avec AWS IoT Core

---

# Rappel de l’objectif

Transformer :

```text
Edge → vérifie périodiquement (polling)
```

en :

```text
Cloud → déclenche l’Edge (event-driven)
```

---

# Partie 1 — Compréhension du changement

---

## ❌ Limite du Pull Model (TP12)

Dans TP12 :

```text
Edge vérifie toutes les 5 minutes
```

👉 problèmes :

* appels inutiles
* latence
* non scalable

---

## Solution introduite

```text
Déclencher uniquement quand nécessaire
```

---

👉 donc :

```text
Git push → événement → Edge
```

---

#  Partie 2 — Architecture finale

---

```text
Git Push
   ↓
GitHub Actions
   ↓
MQTT Publish (TLS)
   ↓
AWS IoT Core
   ↓
Edge connecté (subscriber)
   ↓
deploy.sh
```

---

# Partie 3 — AWS IoT Core

---

## Création du Thing

👉 nom :

```text
edge-device
```

---

## Certificats générés

* device.pem.crt
* private.pem.key
* AmazonRootCA1.pem

---

## Policy minimale

```json
{
  "Effect": "Allow",
  "Action": [
    "iot:Connect",
    "iot:Subscribe",
    "iot:Receive"
  ],
  "Resource": "*"
}
```

---

## Explication

```text
✔ Connect → connexion au broker
✔ Subscribe → écouter topic
✔ Receive → recevoir messages
```

---

# Partie 4 — Script de déploiement

---

```bash
#!/bin/bash

cd /home/vagrant/edge-stack || exit 1

git pull origin main || exit 1

docker compose up -d --build

echo "✅ Deployment done"
```

---

## Rôle

```text
✔ centralise le déploiement
✔ réutilisable
✔ déclenché par événement
```

---

# Partie 5 — MQTT Listener sécurisé

---

## Script

```bash
#!/bin/bash

BROKER="your-endpoint.iot.eu-central-1.amazonaws.com"

mosquitto_sub \
  -h $BROKER \
  -p 8883 \
  --cafile /home/vagrant/certs/AmazonRootCA1.pem \
  --cert /home/vagrant/certs/device.pem.crt \
  --key /home/vagrant/certs/private.pem.key \
  -t deploy/edge | while read msg
do
    if [ "$msg" = "update" ]; then
        echo "🚀 Update triggered"
        /home/vagrant/deploy.sh
    fi
done
```

---

##  Explication

```text
✔ connexion TLS
✔ écoute continue
✔ déclenche action locale
```

---

# Partie 6 — systemd

---

```ini
[Unit]
Description=MQTT Listener AWS
After=network.target

[Service]
User=vagrant
ExecStart=/home/vagrant/mqtt-listener.sh
Restart=always

[Install]
WantedBy=multi-user.target
```

---

## Fonctionnement

```text
✔ écoute en continu
✔ reconnecte automatiquement
✔ robuste
```

---

# Partie 7 — GitHub Actions

---

```yaml
name: Deploy Edge via AWS IoT

on:
  push:
    branches:
      - main

jobs:
  trigger:
    runs-on: ubuntu-latest

    steps:
      - name: Install mosquitto
        run: sudo apt-get update && sudo apt-get install -y mosquitto-clients

      - name: Send MQTT trigger
        run: |
          mosquitto_pub \
            -h ${{ secrets.AWS_IOT_ENDPOINT }} \
            -p 8883 \
            --cafile AmazonRootCA1.pem \
            --cert ci.pem.crt \
            --key ci-private.pem.key \
            -t deploy/edge \
            -m update
```

---

## Rôle

```text
✔ transforme git push en événement MQTT
✔ lien CI/CD → Edge
```

---

#  Partie 8 — Test complet

---

## Flux attendu

```text
git push
   ↓
GitHub Actions
   ↓
MQTT publish
   ↓
Edge reçoit
   ↓
deploy.sh exécuté
```

---

#  Problèmes rencontrés (TRÈS IMPORTANT)

---

## ❌ 1. Mauvais endpoint AWS

```text
connection refused
```

👉 solution :

```text
copier endpoint exact IoT Core
```

---

## ❌ 2. Certificats invalides

```text
TLS error
```

👉 solution :

```text
bon certificat + bonne clé
```

---

## ❌ 3. Policy insuffisante

```text
not authorized
```

👉 solution :

```text
ajouter Subscribe / Receive
```

---

## ❌ 4. Topic incorrect

```text
aucun message reçu
```

👉 solution :

```text
vérifier exact match
```

---

## ❌ 5. Permissions script

```text
permission denied
```

👉 solution :

```bash
chmod +x deploy.sh
```

---

# Partie 9 — Compréhension finale

---

## Avant (TP12)

```text
Edge décide quand vérifier
```

---

## Après (TP13)

```text
Le Cloud déclenche l’Edge
```

---

#  Ce que tu as construit

```text
✔ pipeline CI/CD IoT
✔ communication sécurisée
✔ architecture scalable
✔ système temps réel
```

---

#  Conclusion

---

## Transformation majeure

```text
Polling → Event-driven
```

---

## Résultat

```text
✔ instantané
✔ optimisé
✔ sécurisé
✔ industriel
```

---

#  Point clé

```text
L’Edge ne travaille plus seul
→ il fait partie d’un système connecté
```

---

#  Suite logique

👉 TP14 :

```text
IoT Core → Timestream → Dashboard industriel
IoT Core → Lambda → SNS alert
IoT Core → S3 → Data Lake
```

---

# 🔥 Niveau atteint

```text
TP11 → Docker local
TP12 → DevOps Edge autonome
TP13 → IoT Cloud industriel
```

---
