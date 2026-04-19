# Corrigé — TP 1 : Mise en place de la Stack IoT avec Vagrant

Ce corrigé présente les étapes à suivre pour déployer correctement la stack IoT à l’aide de Vagrant.

---

## 0. Installer Vagrant

Installer Vagrant via le lien suivant :

https://developer.hashicorp.com/vagrant/install

Choisissez le package adapté à votre système d’exploitation, puis installez-le.

---

## 1. Cloner le repository du training

```bash
git clone https://github.com/ubiakoup/IoT-Training.git
```

---

## 2. Se déplacer dans le dossier du TP1

```bash
cd IoT-Training/01_TP_Stack_Setup
```

---

## 3. Accéder au dossier de la stack

```bash
cd iot_stack_ubuntu22
```

---

## 4. Modifier le Vagrantfile (IMPORTANT)

Ouvrir le fichier `Vagrantfile` et adapter les chemins des dossiers synchronisés selon votre machine.

Exemple à modifier :

```ruby
ansible.vm.synced_folder "D:/TECH/Project/Smart-factory-iot-edge-to-cloud/11_TP_Deployment_Ansible", "/home/vagrant/projects", type: "virtualbox"

opc.vm.synced_folder "D:/TECH/Project/Smart-factory-iot-edge-to-cloud/02_TP_run_opcua_plc_simulator", "/home/vagrant/projects", type: "virtualbox"
```

Adapter avec votre chemin local, par exemple :

```ruby
ansible.vm.synced_folder "C:/Users/username/Documents/iot-project/11_TP_Deployment_Ansible", "/home/vagrant/projects", type: "virtualbox"

opc.vm.synced_folder "C:/Users/username/Documents/iot-project/02_TP_run_opcua_plc_simulator", "/home/vagrant/projects", type: "virtualbox"
```

---

## 5. Lancer la stack

```bash
vagrant up
```

---

## 6. Vérifier l’état des machines

```bash
vagrant status
```

---

## 7. Accéder aux machines (optionnel)

```bash
vagrant ssh iot-ansible
vagrant ssh iot-opcua-plc-simulator
vagrant ssh iot-edge
```

---

## 8. Si modification du Vagrantfile

```bash
vagrant provision
```

---

## 9. Gestion des machines

Mettre en pause :

```bash
vagrant suspend
```

Reprendre :

```bash
vagrant resume
```

Redémarrer proprement :

```bash
vagrant reload iot-ansible
```

---

## Bonnes pratiques

* Ne pas utiliser `sudo reboot`
* Utiliser `vagrant reload`
* Adapter les chemins des dossiers synchronisés
* Ne pas interrompre Vagrant

---

La stack est maintenant opérationnelle.
