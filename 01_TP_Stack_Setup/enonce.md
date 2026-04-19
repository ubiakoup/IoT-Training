# TP 1 — Mise en place de la Stack IoT avec Vagrant

## Objectif du TP

L’objectif de ce TP est de permettre à l’apprenant de :

- Mettre en place un environnement de travail complet
- Comprendre les différents serveurs utilisés dans un projet IoT
- Déployer automatiquement une infrastructure avec Vagrant
- Utiliser des dossiers synchronisés pour travailler efficacement
- Préparer les bases pour les prochains travaux pratiques

---

## Contexte

Dans un projet IoT industriel, plusieurs serveurs interviennent pour assurer différentes fonctions :

- génération de données (simulation industrielle)
- traitement des données (edge computing)
- automatisation (orchestration)

Dans ce TP, nous allons simuler cette architecture à l’aide de Vagrant, sans matériel physique.

Nous allons créer trois environnements de travail (trois serveurs), chacun ayant un rôle spécifique.

---

## Architecture de la Stack

La stack déployée met à disposition trois serveurs.

### Serveur Ansible

- OS : Ubuntu
- Rôle :
  - Automatisation
  - Orchestration des autres serveurs
- Technologies :
  - Python
  - Ansible

---

### Serveur OPC UA / PLC

- OS : Ubuntu
- Rôle :
  - Simulation d’un automate industriel (PLC)
  - Génération de données industrielles
- Technologies :
  - Python

---

### Serveur Edge Gateway

- OS : Ubuntu
- Rôle :
  - Traitement des données IoT
  - Hébergement de services
- Technologies :
  - Docker

En entreprise, ce type de machine peut être :
- un Raspberry Pi
- un mini-PC industriel
- ou un serveur physique

---

## Réseau

| Serveur | IP |
|--------|----|
| ansible | 192.168.56.10 |
| opcua-plc | 192.168.56.11 |
| edge | 192.168.56.12 |

---

## Dossiers synchronisés

Certains dossiers de votre machine locale sont synchronisés automatiquement avec les machines virtuelles.

Cela signifie que :
- les fichiers modifiés sur votre PC sont visibles dans la VM
- les fichiers modifiés dans la VM sont visibles sur votre PC

---

### Configuration

Serveur Ansible :

ansible.vm.synced_folder "D:/TECH/Project/Smart-factory-iot-edge-to-cloud/11_TP_Deployment_Ansible", "/home/vagrant/projects", type: "virtualbox"

Serveur OPC UA :

opc.vm.synced_folder "D:/TECH/Project/Smart-factory-iot-edge-to-cloud/02_TP_run_opcua_plc_simulator", "/home/vagrant/projects", type: "virtualbox"

---

## Important — Adapter les chemins

Le chemin utilisé dans cet exemple correspond à la machine de l’instructeur.

Vous devez adapter ces chemins en fonction de l’emplacement du projet sur votre machine.

Exemple :

C:/Users/username/Documents/iot-project

---

## Pourquoi utiliser les dossiers synchronisés

- travailler en local avec votre éditeur
- éviter les copies de fichiers
- tester immédiatement dans la VM
- gagner du temps

---

## Lancement de la stack

cd iot_stack_ubuntu22  

vagrant up  

---

## Vérification

vagrant status  

---

## Accès aux machines

vagrant ssh iot-ansible  
vagrant ssh iot-opcua-plc-simulator  
vagrant ssh iot-edge  

---

## Gestion du cycle de vie des machines (IMPORTANT)

### Modifier la configuration (Vagrantfile)

Si vous modifiez le Vagrantfile :

- ne pas refaire `vagrant up`
- utiliser :

vagrant provision  

👉 Cela permet de mettre à jour la configuration sans recréer les machines.

---

### Mettre en pause les machines

vagrant suspend  

👉 Sauvegarde l’état des machines (comme une hibernation).

---

### Reprendre les machines

vagrant resume  

👉 Redémarre les machines exactement dans l’état précédent.

---

### Redémarrer proprement une machine

vagrant reload iot-ansible  

👉 À utiliser à la place de `sudo reboot`.

---

## Bonnes pratiques importantes

- Ne pas utiliser `sudo reboot` dans les VMs
- Utiliser `vagrant reload`
- Utiliser `vagrant provision` après modification
- Ne pas interrompre les commandes Vagrant
- Toujours attendre la fin d’exécution

---

## Vérifications techniques

ip a  

python3 --version  

docker --version  

---

## Commandes utiles

| Commande | Description |
|--------|------------|
| vagrant up | Démarrer |
| vagrant halt | Arrêter |
| vagrant suspend | Mettre en pause |
| vagrant resume | Reprendre |
| vagrant reload | Redémarrer |
| vagrant provision | Mettre à jour |
| vagrant destroy -f | Supprimer |

---

## Résultat attendu

- trois serveurs fonctionnels
- réseau opérationnel
- Docker fonctionnel
- Python disponible
- Ansible installé
- dossiers synchronisés opérationnels

---

## Suite de la formation

- automatisation avec Ansible
- simulation industrielle
- traitement des données IoT

Vous venez de mettre en place votre première infrastructure IoT virtualisée.