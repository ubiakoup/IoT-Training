````markdown
#  Corrigé — TP 11 : Déploiement IIoT avec Ansible (Vagrant Edition)

---

## Compréhension globale

Dans ce TP, nous avons introduit **Ansible** comme outil d’orchestration dans une architecture IIoT.

👉 Son rôle :

- automatiser le déploiement
- éviter les actions manuelles
- garantir la reproductibilité
- gérer plusieurs machines simultanément

---

## Position dans l’architecture

```text
Ansible (Control Node)
        ↓
Edge Gateway (IoT Stack)
        ↓
OPC UA Simulator (PLC)
````

👉 Ansible pilote toute l’infrastructure via SSH.

---

# Partie 1 — Configuration SSH (Vagrant)

---

##  Spécificité Vagrant

Chaque VM Vagrant possède sa propre clé SSH.

👉 Donc :

* `ssh-copy-id` ❌ ne fonctionne pas
* connexion classique ❌ impossible

---

##  Solution

👉 Utiliser les clés générées automatiquement par Vagrant

---

##  Accès aux clés

Depuis la VM Ansible :

```text
/vagrant/.vagrant/machines/
```

---

## 🔧 Copie des clés

```bash
cp /vagrant/.vagrant/machines/iot-edge/virtualbox/private_key ~/.ssh/edge_key

cp /vagrant/.vagrant/machines/iot-opcua-plc-simulator/virtualbox/private_key ~/.ssh/opcua_plc_simulator_key
```

---

## Permissions (CRITIQUE)

```bash
chmod 600 ~/.ssh/edge_key
chmod 600 ~/.ssh/opcua_plc_simulator_key
```

---

## Erreur typique

```text
UNPROTECTED PRIVATE KEY FILE
```

👉 Cause : permissions incorrectes

---

##  Test SSH

```bash
ssh -i ~/.ssh/edge_key vagrant@192.168.56.12

ssh -i ~/.ssh/opcua_plc_simulator_key vagrant@192.168.56.11
```

---

##  Résultat

✔ connexion réussie
✔ pas de mot de passe

---

#  Partie 2 — Inventory Ansible

---

##  Rôle

Décrire les machines à piloter

---

##  hosts.yml

```yaml
---
all:
  vars:
    ansible_user: vagrant
    ansible_ssh_common_args: '-o StrictHostKeyChecking=no'

  children:
    edge:
      hosts:
        client1:
          ansible_host: 192.168.56.12
          ansible_ssh_private_key_file: /home/vagrant/.ssh/edge_key

    opcua_plc_simulator:
      hosts:
        client2:
          ansible_host: 192.168.56.11
          ansible_ssh_private_key_file: /home/vagrant/.ssh/opcua_plc_simulator_key
```

---

##  Explication

* `ansible_user` → utilisateur distant
* `ansible_host` → IP cible
* `ansible_ssh_private_key_file` → clé SSH

---

#  Partie 3 — Test de connectivité

---

```bash
ansible all -i hosts.yml -m ping
```

---

##  Résultat attendu

```text
client1 | SUCCESS
client2 | SUCCESS
```

---

##  Warning possible

```text
world writable directory
```

✔ Solution :

```bash
chmod 755 ~/projects/Ansible
```

---

#  Partie 4 — Playbook OPC UA Simulator

---

##  deploy_opcua_plc_simulator.yml

```yaml
---
- name: Deploy OPCUA PLC Simulator
  hosts: opcua_plc_simulator
  become: true

  tasks:

    - name: Install python3-venv
      apt:
        name: python3-venv
        state: present
        update_cache: yes

    - name: Create project directory
      file:
        path: /home/vagrant/opcua
        state: directory
        mode: '0755'

    - name: Create virtual environment
      command: python3 -m venv /home/vagrant/opcua/venv

    - name: Copy requirements
      copy:
        src: opcua-plc-simulator/requirements.txt
        dest: /home/vagrant/opcua/requirements.txt

    - name: Install dependencies
      pip:
        requirements: /home/vagrant/opcua/requirements.txt
        virtualenv: /home/vagrant/opcua/venv

    - name: Copy simulator
      copy:
        src: opcua-plc-simulator/opcua_plc_simulation.py
        dest: /home/vagrant/opcua/opcua_plc_simulation.py

    - name: Run simulator
      shell: |
        nohup /home/vagrant/opcua/venv/bin/python /home/vagrant/opcua/opcua_plc_simulation.py &
```

---

#  Partie 5 — Playbook Edge Gateway

---

##  deploy_edge.yml

```yaml
---
- name: "deploy Edge-Gateway services"
  hosts: edge
  become: true
  vars_files:
  - vars.yml

  pre_tasks:
     - name: Install docker compose plugin
       ansible.builtin.apt:
        name: docker-compose-plugin
        state: present
        update_cache: yes

     - name: Install rsync
       ansible.builtin.apt:
        name: rsync
        state: present
        update_cache: yes
  tasks:
     - name: Ensure directories exist
       file:
         path: "{{ item }}"
         state: directory
       loop:
         - /home/vagrant/edge-stack
         - /home/vagrant/data/node-red
         - /home/vagrant/edge-stack/secrets
         - /home/vagrant/data/influxdb
         - /home/vagrant/data/grafana

     - name: Fix Node-RED permissions
       file:
          path: /home/vagrant/data/node-red
          owner: 1000
          group: 1000
          recurse: yes

     - name: Fix InfluxDB permissions
       file:
        path: /home/vagrant/data/influxdb
        owner: 1000
        group: 1000
        recurse: yes


     - name: Fix Grafana permissions
       file:
        path: /home/vagrant/data/grafana
        owner: 472
        group: 472
        recurse: yes

     - name: Copy edge gateway stack
       ansible.posix.synchronize:
        src: ./files/
        dest: /home/vagrant/edge-stack/
        delete: yes
        rsync_opts:
          - "--exclude=.env"
          - "--exclude=secrets"
          - "--exclude=data"
          - "--exclude=node-red"
       
     - name: Remove influx_token if it exists as directory
       file:
        path: /home/vagrant/edge-stack/secrets/influx_token.txt
        state: absent      
      
     - name: Copy secrets (controlled)
       copy:
          src: ./files/secrets/influx_token.txt
          dest: /home/vagrant/edge-stack/secrets/influx_token.txt
          owner: root
          group: root
          mode: '0444'

     - name: Deploy .env file (templated)
       template:
         src: .env.j2
         dest: /home/vagrant/edge-stack/.env
         mode: '0400'

     - name: Run docker compose
       command: docker compose up --build -d
       args:
        chdir: /home/vagrant/edge-stack

  

---

#  Vérifications

---

## Accès aux services

* Node-RED → [http://192.168.56.12:1880](http://192.168.56.12:1880)
* InfluxDB → [http://192.168.56.12:8086](http://192.168.56.12:8086)
* Grafana → [http://192.168.56.12:3000](http://192.168.56.12:3000)

---

##  Résultat attendu

✔ Stack déployée
✔ Données visibles
✔ Dashboards actifs

---

#  Réponses aux questions

---

## 1. Pourquoi SSH ?

👉 Ansible utilise SSH pour exécuter des commandes à distance

---

## 2. Pourquoi ssh-copy-id ne fonctionne pas ?

👉 Vagrant impose ses propres clés SSH

---

## 3. Rôle de l’inventaire ?

👉 Décrire les machines à piloter

---

## 4. Pourquoi playbook ?

👉 Automatiser et structurer les tâches

---

## 5. Ansible vs Docker Compose ?

| Docker Compose | Ansible        |
| -------------- | -------------- |
| local          | multi-machines |
| manuel         | automatisé     |
| limité         | scalable       |

---

#  Conclusion

Dans ce TP, vous avez :

✔ configuré SSH avec Vagrant
✔ connecté plusieurs machines
✔ automatisé un déploiement IIoT
✔ orchestré une infrastructure complète

---

##  Vision finale

```text
1 commande → déploiement complet → multi-machines
```

---
