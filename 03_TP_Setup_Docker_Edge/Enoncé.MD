# TP 03 - Setup Docker sur Edge Gateway

---

## Objectifs pédagogiques

À la fin de ce TP, vous serez capable de :

* Comprendre ce qu’est Docker
* Installer Docker sur un Raspberry Pi
* Exécuter des conteneurs
* Comprendre l’intérêt de la containerisation
* Préparer l’environnement pour le déploiement IoT

---

## Contexte

Dans une architecture IoT moderne, les applications sont conteneurisées.

Docker permet de :

* standardiser les environnements
* simplifier les déploiements
* rendre les systèmes reproductibles

Dans ce projet, toute la stack Edge sera basée sur Docker.

---

# Introduction à Docker

---

## Qu’est-ce que Docker ?

Docker est une technologie de containerisation.

Un conteneur est :

👉 une application + ses dépendances + sa configuration

---

## Différence VM vs Docker

| Machine virtuelle | Docker      |
| ----------------- | ----------- |
| OS complet        | Léger       |
| Lent à démarrer   | Très rapide |
| Consomme beaucoup | Optimisé    |
| Complexe          | Simple      |

---

## Pourquoi Docker dans ce projet ?

Docker permet de :

* déployer facilement plusieurs services
* isoler les composants
* reproduire l’environnement
* scaler l’architecture

👉 C’est une pratique standard en entreprise.

---

# Partie 1 — Installation de Docker

---

## Étape 1 — Télécharger le script

```bash
curl -fsSL https://get.docker.com -o install-docker.sh
```

---

## Étape 2 — Vérifier le script

```bash
cat install-docker.sh
```

---

## Étape 3 — Simulation installation (optionnel)

```bash
sh install-docker.sh --dry-run
```

---

## Étape 4 — Installation

```bash
sudo sh install-docker.sh
```

---

# Partie 2 — Configuration Docker

---

## Ajouter l’utilisateur au groupe Docker

```bash
sudo usermod -aG docker edge
```

---

## Appliquer les changements

```bash
sudo reboot
```

---

👉 Après redémarrage :

Reconnectez-vous en SSH

---

# Partie 3 — Vérification Docker

---

## Vérifier installation

```bash
docker --version
```

---

## Tester Docker

```bash
docker run hello-world
```

---

# Partie 4 — Concepts importants

---

## Image Docker

Une image est un modèle prêt à être exécuté.

---

## Conteneur

Un conteneur est une instance d’une image.

---

## Docker Hub

C’est le registre public des images Docker.

---

## Exemple

```bash
docker run nginx
```

---

# Partie 5 — Commandes essentielles

---

```bash
docker ps
docker ps -a
docker images
docker rm <container_id>
docker rmi <image_id>
```

---

# Analyse

---

## Exercice 1

Qu’est-ce qu’un conteneur Docker ?

---

## Exercice 2

Quelle est la différence entre une image et un conteneur ?

---

## Exercice 3

Pourquoi Docker est-il utilisé dans les architectures IoT ?

---

## Exercice 4

Quels sont les avantages de Docker par rapport à une machine virtuelle ?

---

# Résultat attendu

* Docker est installé
* Les conteneurs fonctionnent
* Les commandes Docker sont comprises

---

# Hints

* Si Docker ne fonctionne pas → vérifier reboot
* Si permission refusée → vérifier groupe docker
* Toujours tester avec `docker run hello-world`

---

# Vision globale

Edge Gateway + Docker = plateforme IoT moderne

---

# Ouverture — Vers des architectures industrielles robustes

Dans les environnements industriels réels :

* haute disponibilité
* scalabilité
* tolérance aux pannes

---

## Limites de Docker seul

Docker ne suffit pas pour gérer :

* plusieurs machines
* des centaines de conteneurs

---

## Introduction à Kubernetes

Kubernetes est un orchestrateur de conteneurs.

---

## Concepts clés

* Cluster
* Node
* Pod

---

## Lien avec Docker

* Docker → crée les conteneurs
* Kubernetes → les orchestre

---

## Pourquoi commencer par Docker ?

Docker est la base.

---

## Dans cette formation

Nous allons :

* utiliser Docker
* utiliser Docker Compose

---

## Évolution possible

Migration vers Kubernetes (niveau entreprise)

---

# Conclusion

Docker est la base de toute architecture moderne.

Prochaine étape :

👉 conteneuriser notre Data Collector (OPC-UA Client)

---
