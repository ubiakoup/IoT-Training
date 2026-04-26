#  TP12 – Corrigé final : Pull Model & séparation provisioning/runtime

---

# 🎯 Objectif du TP

Transformer une architecture couplée :

```text
Ansible → configure + déploie + exécute
```

en une architecture découplée :

```text
Ansible → provisioning (1 fois)
Pull Model → runtime (continu)
```

👉 L’objectif est de **séparer clairement les responsabilités** pour obtenir un système robuste, autonome et industriel.

---

#  Partie 1 — Compréhension du problème

---

## ❌ Pourquoi Ansible ne doit pas tout faire ?

Relancer Ansible à chaque modification pose plusieurs problèmes :

* dépendance à une machine externe
* absence d’autonomie de l’Edge
* déploiements lourds
* non scalable en production

👉 En industrie :

```text
Un Edge doit pouvoir vivre et évoluer seul
```

---

##  Provisioning vs Runtime

| Concept      | Rôle                                           |
| ------------ | ---------------------------------------------- |
| Provisioning | Préparer la machine (Docker, dossiers, config) |
| Runtime      | Exécuter et mettre à jour les applications     |

👉 Mélanger les deux = erreurs + instabilité

---

##  Problèmes rencontrés (réels)

Ce TP a exposé des problèmes classiques en production :

### ❌ 1. Accès Git privé

* SSH non configuré
* blocage du clone

### ❌ 2. Ansible (root) vs runtime (vagrant)

* fichiers créés en root
* service exécuté en vagrant
* conflits de permissions

### ❌ 3. Git “dubious ownership”

* sécurité Git moderne
* repo bloqué

### ❌ 4. Permissions `.env`

* fichier inaccessible
* docker compose échoue

👉 💡 Ces problèmes sont **100% réalistes en entreprise**

---

#  Partie 2 — Playbook Ansible corrigé

---

##  Principe

👉 Ansible doit :

```text
✔ préparer la machine
✔ cloner le projet
✔ installer le mécanisme d’update
✔ lancer une première fois la stack
```

👉 MAIS :

```text
❌ ne gère plus le runtime continu
```

---

##  Playbook final

```yaml
- name: "deploy Edge-Gateway services"
  hosts: edge
  become: true
  vars_files:
    - vars.yml

  pre_tasks:
    - name: Install docker compose plugin
      apt:
        name: docker-compose-plugin
        state: present
        update_cache: yes

  tasks:

    - name: Ensure directories exist
      file:
        path: "{{ item }}"
        state: directory
      loop:
        - /home/vagrant/edge-stack
        - /home/vagrant/edge-stack/secrets
        - /home/vagrant/data/influxdb
        - /home/vagrant/data/grafana

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

    - name: Remove existing edge-stack directory
      file:
        path: /home/vagrant/edge-stack
        state: absent

    - name: Clone project repository
      git:
        repo: "{{ git_repo_url }}"
        dest: /home/vagrant/edge-stack
        version: main
        key_file: /home/vagrant/.ssh/id_ed25519
        accept_hostkey: yes
      become_user: vagrant

    - name: Ensure ownership is correct
      file:
        path: /home/vagrant/edge-stack
        owner: vagrant
        group: vagrant
        recurse: yes

    - name: Copy secrets
      copy:
        src: ./files/secrets/influx_token.txt
        dest: /home/vagrant/edge-stack/secrets/influx_token.txt
        owner: root
        group: root
        mode: '0444'

    - name: Deploy .env file
      template:
        src: .env.j2
        dest: /home/vagrant/edge-stack/.env
        owner: vagrant
        group: vagrant
        mode: '0600'

    - name: Deploy pull-update script
      copy:
        src: ./files/pull-update.sh
        dest: /home/vagrant/pull-update.sh
        owner: vagrant
        group: vagrant
        mode: '0755'

    - name: Deploy systemd service
      copy:
        src: ./files/iiot-pull.service
        dest: /etc/systemd/system/iiot-pull.service

    - name: Reload systemd
      command: systemctl daemon-reload

    - name: Enable service
      systemd:
        name: iiot-pull.service
        enabled: yes

    - name: Start service
      systemd:
        name: iiot-pull.service
        state: started

    - name: Initial docker compose up
      command: docker compose up -d --build
      args:
        chdir: /home/vagrant/edge-stack
```

---

# 🔄 Partie 3 — Script Pull Model (optimisé)

```bash
#!/bin/bash

set -e

PROJECT_DIR="/home/vagrant/edge-stack"

export PATH=/usr/bin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
export GIT_SSH_COMMAND="ssh -i /home/vagrant/.ssh/id_ed25519 -o StrictHostKeyChecking=no"

echo "📁 Moving to project directory..."
cd $PROJECT_DIR || exit 1

OLD_COMMIT=$(git rev-parse HEAD)

echo "🔄 Pull latest version..."
git pull origin main

NEW_COMMIT=$(git rev-parse HEAD)

if [ "$OLD_COMMIT" != "$NEW_COMMIT" ]; then
    echo "🚀 Changes detected, deploying..."
    docker compose up -d --build
else
    echo "✅ No changes, skipping deploy"
fi

echo "🧹 Cleanup..."
docker image prune -f

echo "✅ Update done"
```

---

## 🧠 Explication importante

👉 `docker compose up -d` est **idempotent** :

```text
✔ ne recrée les containers QUE si nécessaire
✔ ne duplique pas
✔ conserve les volumes
```

👉 La comparaison des commits :

```text
✔ évite les rebuild inutiles
✔ améliore les performances
```

---

# ⚙️ Partie 4 — Service systemd

```ini
[Unit]
Description=IIoT Pull Model Service
After=network.target

[Service]
User=vagrant
WorkingDirectory=/home/vagrant/edge-stack
ExecStart=/home/vagrant/pull-update.sh
Restart=always
RestartSec=300

[Install]
WantedBy=multi-user.target
```

---

## 🧠 Fonctionnement réel

```text
run → script → exit → attente 5 min → restart
```

👉 Ce service :

* ne tourne pas en continu
* exécute un job périodique
* remplace un cron avancé

---

# 🧪 Partie 5 — Vérification

```bash
systemctl status iiot-pull.service
journalctl -u iiot-pull.service -f
```

---

## ✔ Résultat attendu

* service actif
* exécution toutes les 5 minutes
* git pull OK
* docker OK

---

# ⚠️ Erreurs rencontrées

---

## ❌ SSH GitHub

→ clone impossible

## ❌ Permissions root/vagrant

→ conflits

## ❌ Git ownership

→ blocage

## ❌ .env inaccessible

→ docker échoue

## ❌ rebuild constant

→ inefficacité

---

# 🧠 Bonnes pratiques

```text
✔ runtime user ≠ root
✔ secrets hors Git
✔ docker idempotent
✔ séparation des responsabilités
```

---

#  Conclusion

---

## Avant

```text
Ansible fait tout
```

---

## Après

```text
Ansible → provisioning
Pull Model → runtime
```

---

## Résultat

```text
✔ Edge autonome
✔ mise à jour automatique
✔ architecture propre
✔ base industrielle
```

---

#  Point clé

```text
Le Pull Model ne remplace pas Ansible
Il complète le système
```

---

#  Limite du Pull Model

```text
Le système vérifie toutes les 5 minutes (polling)

✔ consommation inutile
✔ latence possible
```

---

# Transition vers TP13

👉 Prochaine étape :

```text
Remplacer le polling par un modèle event-driven
```

---

## 🔁 Évolution

```text
TP12 → vérifie périodiquement
TP13 → réagit à un événement (MQTT / AWS IoT Core)
```

---

## 🎯 Objectif futur

```text
Edge → connecté au cloud
→ déclenché en temps réel
→ architecture IoT industrielle complète
```
