#  TP14 – Pipeline IoT vers un Data Lake avec AWS IoT Core

---

#  Objectifs

Dans ce TP, vous allez faire évoluer votre architecture afin de :

* connecter votre Edge au cloud via un **bridge MQTT**
* centraliser les données industrielles dans le cloud
* mettre en place un **data lake basé sur S3**
* comprendre le rôle des **AWS IoT Rules**
* construire une architecture IoT scalable et industrielle

---

#  Contexte (Lien avec TP12 & TP13)

Dans les TP précédents :

---

##  TP12 – Pull Model

```text id="ctx1"
Edge autonome qui vérifie périodiquement les mises à jour
```

---

##  TP13 – Event-Driven

```text id="ctx2"
Git push → événement MQTT → déclenchement du déploiement
```

---

👉 Vous avez donc construit :

```text id="ctx3"
✔ un Edge autonome
✔ capable de réagir à des événements cloud
✔ connecté à AWS IoT Core
```

---

#  Nouvelle étape

Jusqu’ici, votre Edge :

```text id="ctx4"
réagit à des événements mais ne valorise pas ses données
```

---

##  Problématique

Les données industrielles :

```text id="ctx5"
restent locales (dans le broker MQTT)
```

👉 Cela pose plusieurs problèmes :

* aucune centralisation
* aucune historisation
* impossibilité d’analyse
* aucune exploitation data (ML, dashboards, alerting)

---

# Problème fondamental

```text id="ctx6"
Les données existent… mais elles ne sont pas exploitées
```

---

#  Objectif du TP

Construire un pipeline de données :

```text id="ctx7"
Edge → MQTT → AWS IoT → S3 (Data Lake)
```

---

# 🧱 Architecture cible

```text id="ctx8"
MQTT Broker local
        ↓
MQTT Bridge (Mosquitto)
        ↓
AWS IoT Core
        ↓
IoT Rule
        ↓
S3 (Data Lake)
```

---

#  Concepts introduits

Dans ce TP, vous allez découvrir :

* MQTT Bridge (connexion broker → cloud)
* AWS IoT Core comme point central
* IoT Rules pour router les données
* S3 comme base de Data Lake
* structuration des données IoT

---

#  Point important

Votre architecture contient déjà :

```text id="ctx9"
un broker MQTT local (factory/#/+)
```

👉 Vous ne devez PAS le remplacer.

👉 Vous devez :

```text id="ctx10"
le connecter au cloud via un bridge
```

---

# Partie 1 — Mise en place du Bridge MQTT

---

## Objectif

Permettre au broker local d’envoyer ses données vers AWS IoT Core.

---

## Travail demandé

* créer un **Thing AWS IoT**

* récupérer :

  * certificat
  * clé privée
  * certificat racine (CA)
  * endpoint AWS IoT

* configurer un **bridge Mosquitto**

---

##  Résultat attendu

```text id="ctx11"
Les messages publiés localement sont transmis vers AWS IoT Core
```

---

#  Partie 2 — Configuration du broker Mosquitto

---

##  Objectif

Configurer un broker capable de :

```text id="ctx12"
✔ recevoir des données locales
✔ les relayer vers AWS IoT
```

---

## Travail demandé

* créer une structure de configuration Mosquitto
* gérer les certificats
* configurer la connexion sécurisée TLS
* définir les topics à relayer

---

##  Résultat attendu

```text id="ctx13"
Le broker local agit comme passerelle vers le cloud
```

---

# Partie 3 — Déploiement avec Ansible

---

## Objectif

Automatiser le déploiement du bridge MQTT sur l’Edge.

---

## Travail demandé

* adapter le playbook `deploy_edge.yml`
* créer les dossiers nécessaires
* déployer :

  * configuration Mosquitto
  * certificats AWS
* adapter le `docker-compose.yml`

---

##  Point critique

```text id="ctx14"
Ne pas confondre :
✔ certificats du MQTT Listener (TP13)
✔ certificats du MQTT Bridge (TP14)
```

---

##  Résultat attendu

```text id="ctx15"
Le broker Mosquitto fonctionne dans Docker avec le bridge actif
```

---

#  Partie 4 — Création du Data Lake S3

---

##  Objectif

Stocker les données IoT dans un stockage centralisé.

---

## Travail demandé

* créer un bucket S3
* définir une policy permettant l’écriture
* réfléchir à la structuration des données

---

## Résultat attendu

```text id="ctx16"
Les données IoT sont stockées dans S3
```

---

#  Partie 5 — Création d’une IoT Rule

---

##  Objectif

Router automatiquement les données MQTT vers S3.

---

## Travail demandé

* créer une IoT Rule
* écrire une requête SQL adaptée
* configurer une action S3
* structurer le chemin des fichiers

---

## Résultat attendu

```text id="ctx17"
Chaque message MQTT génère un fichier structuré dans S3
```

---

#  Partie 6 — Test complet

---

## Scénario attendu

```text id="ctx18"
publish MQTT → bridge → AWS IoT → S3
```

---

## Travail demandé

* publier un message MQTT local
* vérifier la réception dans AWS IoT
* vérifier l’écriture dans S3

---

#  Analyse

Réfléchissez aux questions suivantes :

1. Pourquoi utiliser un bridge MQTT au lieu de connecter directement chaque service ?
2. Pourquoi S3 est adapté pour un data lake IoT ?
3. Quel est le rôle des IoT Rules ?
4. Pourquoi structurer les données par topic ?

---

#  Points de vigilance

* certificats TLS (chemins, permissions)
* configuration du bridge Mosquitto
* cohérence des topics MQTT
* permissions AWS (S3 / IoT)
* séparation des rôles (listener vs bridge)

---

#  Résultat attendu

À la fin du TP, vous devez obtenir :

```text id="ctx19"
✔ un broker MQTT connecté au cloud
✔ un bridge fonctionnel
✔ une ingestion de données IoT
✔ un stockage dans S3
✔ une architecture scalable
```

---

#  Conclusion

Vous avez transformé votre système :

---

## Avant

```text id="ctx20"
Edge isolé avec données locales
```

---

## Après

```text id="ctx21"
Edge connecté → Cloud → Data Lake
```

---

## Résultat

```text id="ctx22"
✔ données centralisées
✔ base analytique
✔ architecture industrielle
✔ prêt pour data engineering
```

---

#  Transition

Ce TP introduit :

```text id="ctx23"
la gestion des données IoT
```

👉 Prochaine étape :

```text id="ctx24"
TP15 → traitement temps réel (Lambda + SNS)
```

---

#  À retenir

```text id="ctx25"
Une architecture IoT ne s’arrête pas à collecter des données
→ elle doit les exploiter
```

---
