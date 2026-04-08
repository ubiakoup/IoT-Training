# Corrigé - TP 03 Setup Docker sur Edge Gateway

---

## Compréhension globale

Dans ce TP, nous avons installé Docker sur notre Edge Gateway.

Docker permet de conteneuriser les applications afin de :

* simplifier le déploiement
* garantir la reproductibilité
* isoler les services

---

## Validation des étapes

---

### Installation Docker

La commande suivante doit avoir été exécutée :

```bash
sudo sh install-docker.sh
```

---

### Ajout utilisateur

```bash
sudo usermod -aG docker edge
sudo reboot
```

👉 Cela permet d’exécuter Docker sans sudo.

---

### Vérification

```bash
docker --version
```

---

### Test fonctionnel

```bash
docker run hello-world
```

👉 Si le message s’affiche, Docker fonctionne correctement.

---

## Exercice 1

### Qu’est-ce qu’un conteneur Docker ?

Un conteneur est un environnement isolé contenant :

* une application
* ses dépendances
* sa configuration

---

## Exercice 2

### Différence image / conteneur

* Image : modèle
* Conteneur : instance en cours d’exécution

---

## Exercice 3

### Pourquoi Docker en IoT ?

Docker permet de :

* déployer facilement sur plusieurs machines
* isoler les composants
* reproduire l’environnement

---

## Exercice 4

### Avantages vs VM

Docker est :

* plus léger
* plus rapide
* plus simple à déployer

---

## Problèmes courants

---

### Permission denied

Solution :

```bash
sudo usermod -aG docker edge
sudo reboot
```

---

### Docker ne démarre pas

```bash
sudo systemctl start docker
```

---

### Vérification service

```bash
sudo systemctl status docker
```

---

## Vision globale

```text
Edge Gateway → Docker → Conteneurs IoT
```

---

## Conclusion

Docker est maintenant installé et fonctionnel.

👉 L’Edge Gateway est prêt pour :

* déploiement de services
* architecture IoT conteneurisée

---

## Prochaine étape

👉 Conteneuriser le Data Collector OPC-UA

---
