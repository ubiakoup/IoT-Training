# Corrigé — TP 2 : Simulation OT avec OPC-UA

---

## Accès à la machine OPC UA

```bash
cd iot_stack_ubuntu22
vagrant ssh iot-opcua-plc-simulator
````

---

## Accès au projet

```bash
cd /home/vagrant/projects
ls
```

---

## Vérification de l’environnement

```bash
python3 --version
python3 -m pip --version
```

---

## Création de l’environnement virtuel (IMPORTANT)

⚠️ Le dossier `/home/vagrant/projects` est un dossier partagé (Windows ↔ Linux)

👉 Il ne supporte pas correctement les environnements virtuels Python

👉 Il faut créer le venv dans le HOME Linux

---

## Création du venv

```bash
cd /home/vagrant
python3 -m venv venv
```

---

## Activation du venv

```bash
source /home/vagrant/venv/bin/activate
```

---

## Retour dans le projet

```bash
cd /home/vagrant/projects
```

---

## Création du fichier requirements.txt

```bash
nano requirements.txt
```

Contenu :

```txt
opcua
cryptography
```

---

## Installation des dépendances

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Vérification des packages

```bash
pip list
```

---

## Lancement du simulateur OPC-UA

```bash
python3 opcua_plc_simulation.py
```

---

# 📘 Lecture recommandée (TRÈS IMPORTANT)

Pour bien comprendre le fonctionnement du simulateur industriel, il est fortement recommandé de lire le document suivant :

```bash
cat opcua_plc_simulation.MD
```

👉 Ce document explique en détail :

* l’architecture industrielle simulée
* les différents PLC
* les capteurs simulés
* les modes de fonctionnement (normal / dégradation / panne)
* la logique de génération des données

👉 C’est une étape clé pour comprendre la suite des TP.

---

# Compréhension globale

Dans ce TP, nous avons mis en place un environnement permettant de simuler une couche OT (Operational Technology).

Cette couche représente les machines industrielles (PLC) qui produisent des données.

Grâce à Python et au protocole OPC-UA, nous avons pu simuler ces machines et exposer leurs données.

---

## Vérification finale

Si tout fonctionne :

* Python est installé
* Le venv est actif
* Les dépendances sont installées
* Le serveur OPC-UA tourne

---

## Exercice 1

### Pourquoi utilise-t-on un environnement virtuel ?

Un environnement virtuel permet de :

* isoler les dépendances d’un projet
* éviter les conflits entre versions de librairies
* ne pas impacter le système global

👉 Cela garantit que le projet reste reproductible et stable.

---

## Exercice 2

### Quel est le rôle de la bibliothèque OPC-UA ?

La bibliothèque OPC-UA permet de :

* créer un serveur OPC-UA
* exposer des données industrielles
* simuler un automate industriel (PLC)

👉 Elle joue un rôle clé dans la communication entre les machines et les systèmes informatiques.

---

## Exercice 3

### Que représente le simulateur PLC ?

Le simulateur PLC représente :

* une machine industrielle
* un automate réel

Il génère des données telles que :

* température
* vibration
* courant
* pression

👉 Ces données seront utilisées dans les prochains TP.

---

## Exercice 4

### Pourquoi simuler un environnement OT ?

Dans un contexte réel :

* les machines industrielles sont coûteuses
* elles ne sont pas toujours accessibles


👉 La simulation permet :

* de reproduire un environnement réel
* de tester sans risque
* d’apprendre plus facilement

---

## Compréhension du fonctionnement

Le script Python :

1. génère des données
2. crée un serveur OPC-UA
3. expose les données
4. permet à d’autres systèmes de les lire

👉 Il constitue la source de données de toute l’architecture.


## Conclusion

👉 Ce TP met en place la première brique du système :

➡️ la génération de données industrielles

Ces données seront utilisées dans les prochains TP pour :

* collecte
* traitement
* stockage
* visualisation



