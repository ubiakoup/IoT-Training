#  TP12 – Restructuration du déploiement & Pull Model

---

# 🎯 Objectifs

Dans ce TP, vous allez faire évoluer votre architecture afin de :

* Séparer clairement le **provisioning** et le **runtime**
* Comprendre les limites d’un déploiement basé uniquement sur Ansible
* Mettre en place un mécanisme de mise à jour automatique
* Rendre votre Edge **autonome et maintenable**
* Faire face à des **problèmes réels de déploiement (Git, permissions, systemd)**

---

# 🧠 Contexte

Dans le TP11, vous avez déployé une stack IIoT complète avec :

* Ansible
* Docker Compose
* Node-RED
* InfluxDB
* Grafana

👉 Le système fonctionne correctement.

---

##  Limite actuelle

```text id="ctx1"
Les mises à jour dépendent entièrement d’Ansible
```

👉 Cela implique :

* relancer un playbook à chaque modification
* dépendance à une machine externe
* absence d’autonomie
* architecture non réaliste en production

---

#  Problématique

Dans le TP11, Ansible gère :

* la configuration
* le déploiement
* l’exécution

👉 On mélange donc :

```text id="ctx2"
Provisioning + Runtime
```

👉 Ce modèle est fragile et non scalable.

---

#  Objectif du TP

Faire évoluer l’architecture vers :

```text id="ctx3"
Ansible → provisioning (une seule fois)
Pull Model → runtime (continu)
```

---

#  Rôle d’Ansible

Dans ce TP, Ansible doit uniquement :

* installer les outils
* créer les dossiers
* gérer les permissions
* cloner le projet
* gérer les secrets
* installer le mécanisme de mise à jour

👉 Il ne doit plus piloter le runtime.

---

# 🔄 Principe du Pull Model

Le Pull Model consiste à laisser l’Edge :

* récupérer les mises à jour depuis Git
* décider lui-même quand se mettre à jour
* redéployer la stack automatiquement

👉 L’Edge devient **autonome**.

---

#  Attention (très important)

Ce TP va volontairement vous confronter à des problèmes réels :

```text id="ctx_real"
✔ accès Git privé
✔ gestion des clés SSH
✔ conflits de permissions (root vs user)
✔ erreurs systemd
✔ gestion des fichiers sensibles (.env)
```

👉 Ces problèmes font partie intégrante du TP.

---

#  Partie 1 — Analyse

Réfléchissez au fonctionnement du TP11.

### Questions :

1. Pourquoi relancer Ansible à chaque modification est-il problématique ?
2. Quelle différence entre provisioning et runtime ?
3. Quels risques si un seul outil gère tout ?

---

#  Partie 2 — Adaptation du playbook Ansible

Vous allez modifier `deploy_edge.yml`.

👉 Objectif :

```text id="ctx4"
Transformer Ansible en outil de provisioning uniquement
```

---

## ✔️ À conserver

* préparation du système
* création des dossiers
* gestion des permissions
* gestion des secrets
* déploiement des fichiers

---

## ❌ À supprimer

* toute logique de runtime continu
* toute dépendance à Ansible pour les mises à jour

---

## ➕ À ajouter

* clonage du projet depuis Git
* installation du script Pull Model
* création d’un service systemd
* activation automatique du service

---

## ⚠️ Points de vigilance

👉 Faites particulièrement attention à :

* l’utilisateur qui exécute Git
* les permissions des fichiers
* l’accès au dépôt privé
* l’emplacement du projet

---

# 🔄 Partie 3 — Mise en place du Pull Model

Vous allez créer un script de mise à jour.

Ce script doit :

* se positionner dans le bon répertoire
* récupérer les dernières modifications
* redéployer la stack Docker

---

##  Comportement attendu

👉 Le système doit :

```text id="ctx5"
✔ vérifier régulièrement les mises à jour
✔ redéployer uniquement si nécessaire
✔ éviter les opérations inutiles
```

---

#  Partie 4 — Automatisation avec systemd

Vous allez :

* créer un service systemd
* automatiser l’exécution du script
* gérer les redémarrages

---

##  Objectif

```text id="ctx6"
Rendre le système autonome sans intervention humaine
```

---

#  Partie 5 — Vérification

Vérifiez que :

* le service systemd est actif
* le script s’exécute sans erreur
* Git fonctionne correctement
* la stack est mise à jour automatiquement

---

##  Tests recommandés

* modifier le dépôt Git
* observer les logs systemd
* vérifier le comportement sans modification

---

#  Organisation du projet

Toutes les opérations doivent être réalisées dans :

```bash id="ctx7"
/home/vagrant/edge-stack
```

👉 Ce dossier est la **source de vérité du runtime**.

---

#  Analyse finale

1. Pourquoi le Pull Model ne remplace-t-il pas Ansible ?
2. Pourquoi séparer provisioning et runtime ?
3. Quel est le rôle de systemd dans cette architecture ?
4. Pourquoi les permissions sont-elles critiques dans ce TP ?

---

#  Résultat attendu

À la fin du TP :

```text id="ctx8"
✔ Edge autonome
✔ mise à jour automatique
✔ architecture découplée
✔ système maintenable
```

---

#  Conclusion

Vous avez transformé une stack fonctionnelle en un système :

```text id="ctx9"
✔ autonome
✔ robuste
✔ évolutif
✔ proche d’un environnement industriel réel
```

---

#  Transition

Ce TP introduit une limite :

```text id="ctx10"
Le système vérifie toutes les 5 minutes
```

👉 Prochaine étape :

```text id="ctx11"
Passer à un modèle event-driven (TP13)
```

---
