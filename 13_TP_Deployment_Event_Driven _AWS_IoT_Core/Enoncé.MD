Parfait — là tu passes clairement en **architecture IoT industrielle complète AWS** 👍
👉 On va verrouiller **TP13 dans la logique AWS IoT Core**, pour que tout le reste (Timestream, Lambda, SNS, S3) s’enchaîne naturellement.

---

# 📘 TP13 – Énoncé (VERSION AWS INDUSTRIELLE)

## Déploiement Event-Driven avec AWS IoT Core

---

# 🎯 Objectifs pédagogiques

À la fin de ce TP, vous serez capable de :

* Utiliser **AWS IoT Core** comme broker MQTT sécurisé
* Connecter un Edge via certificat X.509
* Déclencher un déploiement via un événement MQTT
* Intégrer un pipeline CI/CD avec IoT Core
* Comprendre une architecture IoT cloud industrielle

---

# 🧠 Contexte

Dans un environnement réel :

```text
Edge n’a PAS d’IP publique
```

👉 donc :

```text
Edge → se connecte au Cloud
Cloud → envoie des événements
```

---

# 🧱 Architecture

```text
Git Push
   ↓
GitHub Actions
   ↓
AWS IoT Core (MQTT TLS)
   ↓
Edge (subscriber sécurisé)
   ↓
deploy.sh
   ↓
docker compose
```

---

# 🛠️ Partie 1 — Créer un Thing AWS IoT

Dans AWS :

1. Aller dans **AWS IoT Core**
2. Créer un **Thing** → `edge-device`
3. Générer :

   * certificat
   * clé privée
   * CA Amazon
4. Attacher une policy MQTT :

```json
{
  "Effect": "Allow",
  "Action": ["iot:Connect","iot:Subscribe","iot:Receive"],
  "Resource": "*"
}
```

---

# 🛠️ Partie 2 — Script de déploiement Edge

```bash
nano /home/vagrant/deploy.sh
```

```bash
#!/bin/bash

cd /home/vagrant/edge-stack || exit 1

git pull origin main || exit 1

docker compose up -d --build

echo "✅ Deployment done"
```

---

# 📡 Partie 3 — MQTT Listener sécurisé

```bash
nano /home/vagrant/mqtt-listener.sh
```

```bash
#!/bin/bash

BROKER="your-endpoint.iot.eu-central-1.amazonaws.com"

mosquitto_sub \
  -h $BROKER \
  -p 8883 \
  --cafile AmazonRootCA1.pem \
  --cert device.pem.crt \
  --key private.pem.key \
  -t deploy/edge | while read msg
do
    if [ "$msg" = "update" ]; then
        /home/vagrant/deploy.sh
    fi
done
```

---

# ⚙️ Partie 4 — Service systemd

```ini
[Unit]
Description=IIoT AWS Event Deployment
After=network.target

[Service]
User=vagrant
ExecStart=/home/vagrant/mqtt-listener.sh
Restart=always

[Install]
WantedBy=multi-user.target
```

---

# ☁️ Partie 5 — GitHub Actions

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
        run: sudo apt-get install -y mosquitto-clients

      - name: Send MQTT trigger
        run: |
          mosquitto_pub \
            -h YOUR_AWS_ENDPOINT \
            -p 8883 \
            --cafile AmazonRootCA1.pem \
            --cert ci.pem.crt \
            --key ci-private.pem.key \
            -t deploy/edge \
            -m update
```

---

# 🧪 Partie 6 — Test

```text
git push → CI → MQTT → Edge → deploy
```

---

# 🔍 Analyse

* Pourquoi TLS est obligatoire ?
* Pourquoi Edge initie la connexion ?
* Quel est le rôle du broker ?

---

---

# 📘 TP13 – Corrigé (VERSION AWS)

---

# 🧠 Analyse

---

## Pourquoi AWS IoT Core ?

```text
✔ sécurisé (TLS)
✔ scalable
✔ gestion des devices
✔ intégration cloud native
```

---

## Fonctionnement

```text
Edge → connecté en continu au broker AWS
CI/CD → envoie un message MQTT
Edge → reçoit → déclenche
```

---

# 🔐 Sécurité

* certificats X.509
* policies MQTT
* aucune IP publique nécessaire

---

# ⚙️ MQTT sécurisé

```bash
mosquitto_sub \
  -h endpoint \
  -p 8883 \
  --cert device.pem.crt \
  --key private.pem.key \
  --cafile AmazonRootCA1.pem
```

---

# ⚠️ Erreurs fréquentes

---

## ❌ Utiliser localhost

👉 impossible avec AWS

---

## ❌ Mauvais certificats

👉 connexion refusée

---

## ❌ Mauvaise policy

👉 pas de subscribe/publish

---

## ❌ Mauvais endpoint

👉 vérifier région AWS

---

# 🧠 Conclusion

---

## Avant

```text
Edge vérifie (polling)
```

---

## Maintenant

```text
Cloud déclenche (event)
```

---

## Résultat

* déploiement instantané
* architecture sécurisée
* compatible industrie

---

# 🚀 Suite logique (TP14+)

👉 maintenant tu peux enchaîner :

* IoT Rule → Timestream
* IoT Rule → Lambda → SNS
* IoT Rule → S3 (data lake)

👉 là tu construis :

```text
Edge → AWS IoT → Data pipeline → ML
```

---

# 💬 À retenir

```text
AWS IoT Core = cœur de ton architecture IoT
```

---

Si tu veux, prochain TP :

👉 **TP14 : IoT Rules → Timestream + dashboard industriel**

(là tu touches du vrai Smart Factory 🔥)
