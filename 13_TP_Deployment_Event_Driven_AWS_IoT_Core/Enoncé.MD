# 📘 TP13 – Passage à une architecture Event-Driven avec AWS IoT Core

---

# 🎯 Objectifs

Dans ce TP, vous allez faire évoluer votre architecture afin de :

* comprendre les limites du Pull Model (TP12)
* supprimer le mécanisme de polling
* mettre en place une architecture **event-driven**
* déclencher un déploiement via un **git push**
* introduire **AWS IoT Core** comme broker MQTT sécurisé
* construire une base d’architecture IoT industrielle

---

# 🧠 Contexte (Lien avec TP12)

Dans le TP12, vous avez construit un Edge autonome basé sur :

* un script `pull-update.sh`
* un service systemd
* une vérification périodique (toutes les 5 minutes)

👉 Architecture :

```text
Edge → vérifie Git → déploie si changement
```

---

## ✅ Ce qui fonctionne bien

* autonomie de l’Edge
* mise à jour automatique
* simplicité

---

## ❗ Limites importantes

```text
Le système vérifie même lorsqu’il n’y a rien à faire
```

---

👉 Cela entraîne :

* consommation CPU inutile
* appels réseau inutiles
* latence (jusqu’à 5 minutes)
* inefficacité à grande échelle

---

## 🧠 Problème fondamental

```text
Le système prend l’initiative → ce n’est pas optimal
```

---

👉 En architecture moderne :

```text
Ce n’est pas le device qui décide
→ c’est le système qui déclenche
```

---

# 🔄 Changement de paradigme

---

## ❌ Avant (TP12)

```text
Polling
Edge → "y a-t-il une mise à jour ?"
```

---

## ✅ Après (TP13)

```text
Event-driven
"Une mise à jour existe → déclencher immédiatement"
```

---

# 🎯 Objectif du TP

Mettre en place une architecture où :

```text
Un git push déclenche automatiquement un déploiement sur l’Edge
```

---

# 🧱 Architecture cible

```text
Git Push
   ↓
GitHub Actions
   ↓
MQTT Publish (TLS)
   ↓
AWS IoT Core
   ↓
Edge (subscriber sécurisé)
   ↓
deploy.sh
   ↓
docker compose
```

---

# 🔑 Concept clé

```text
On passe d’un système qui vérifie
→ à un système qui réagit
```

---

# 🧠 Contrainte industrielle importante

Dans un environnement réel :

```text
L’Edge n’a PAS d’IP publique
```

👉 donc :

```text
✔ l’Edge initie la connexion vers le cloud
✔ le cloud envoie des événements
```

---

# 🛠️ Partie 1 — AWS IoT Core

Vous devez :

* créer un **Thing**
* générer des certificats X.509
* attacher une policy MQTT

---

## 🎯 Objectif

```text
Permettre à l’Edge de se connecter de manière sécurisée
```

---

# 🛠️ Partie 2 — Script de déploiement

Créer un script :

```bash
deploy.sh
```

👉 rôle :

```text
mettre à jour et redéployer la stack
```

---

# 📡 Partie 3 — MQTT Listener sécurisé

Vous devez créer un listener qui :

* se connecte à AWS IoT Core (TLS)
* s’abonne à un topic
* écoute en continu
* déclenche `deploy.sh`

---

## 🎯 Objectif

```text
Transformer un message MQTT en action système
```

---

# ⚙️ Partie 4 — Automatisation avec systemd

Créer un service systemd pour :

* démarrer automatiquement le listener
* garantir sa disponibilité

---

# ☁️ Partie 5 — Intégration GitHub

Vous devez :

* créer un workflow GitHub Actions
* envoyer un message MQTT après un `git push`

---

## 🎯 Objectif

```text
Connecter CI/CD → Edge
```

---

# 🧪 Partie 6 — Test complet

Vous devez valider le flux :

```text
git push → MQTT → Edge → déploiement
```

---

# 🔍 Analyse

Répondez aux questions suivantes :

1. Pourquoi le polling n’est-il pas adapté à grande échelle ?
2. Pourquoi MQTT est-il utilisé dans les architectures IoT ?
3. Pourquoi l’Edge doit-il initier la connexion ?
4. Quel est le rôle de GitHub Actions dans ce système ?

---

# ⚠️ Points de vigilance

* certificats TLS
* permissions système
* accès réseau
* cohérence des topics MQTT

---

# ✅ Résultat attendu

À la fin du TP :

```text
✔ déploiement déclenché par événement
✔ suppression du polling
✔ réaction immédiate
✔ architecture cloud-ready
```

---

# 🚀 Conclusion

---

## Avant

```text
Edge autonome mais passif
```

---

## Après

```text
Edge connecté et piloté par le cloud
```

---

## Résultat

```text
✔ temps réel
✔ scalable
✔ sécurisé
✔ industriel
```

---

# 🔥 Transition

Ce TP introduit :

```text
Communication Edge ↔ Cloud
```

👉 Prochaines étapes :

* IoT → Timestream
* IoT → Lambda
* IoT → SNS
* IoT → S3

---

# 💬 À retenir

```text
Le polling est une solution simple
mais l’event-driven est une solution industrielle
```

---
