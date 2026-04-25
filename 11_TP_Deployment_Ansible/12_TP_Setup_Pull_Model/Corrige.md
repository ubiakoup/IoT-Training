#  TP12 – Corrigé : Restructuration du déploiement & Pull Model

---

##  Rappel de l’objectif

Dans ce TP, il fallait transformer l’architecture suivante :

```text
Ansible → configure + déploie + exécute
```

en :

```text
Ansible → provisioning (1 fois)
Pull Model → runtime (continu)
```

👉 L’objectif n’est pas de remplacer Ansible, mais de **séparer les responsabilités**.

---

#  Partie 1 — Analyse

---

##  Pourquoi relancer Ansible à chaque modification est une mauvaise pratique ?

* Cela crée une dépendance à un outil externe
* Le système n’est pas autonome
* Chaque mise à jour devient lourde et risquée
* Cela ne scale pas dans un environnement industriel

👉 En production, un Edge doit pouvoir évoluer seul.

---

##  Différence entre provisioning et runtime

| Concept      | Rôle                                                  |
| ------------ | ----------------------------------------------------- |
| Provisioning | Préparer le système (installations, dossiers, config) |
| Runtime      | Exécuter et mettre à jour les applications            |

👉 Mélanger les deux rend le système fragile.

---

##  Risque si un seul outil gère tout

* perte de contrôle
* couplage fort
* difficulté de maintenance
* erreurs lors des mises à jour

---

#  Partie 2 — Adaptation du playbook Ansible

---

## ❌ Erreur classique

Garder ceci dans Ansible :

```yaml
docker compose up -d --build
```

👉 Mauvais car :

```text
Ansible continue de gérer le runtime
```

---

##  Correction

👉 Supprimer toute commande liée à Docker runtime.

---

##  Playbook corrigé (simplifié)

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


  tasks:

    # -------------------------------
    # Directories
    # -------------------------------
    - name: Ensure directories exist
      file:
        path: "{{ item }}"
        state: directory
      loop:
        - /home/vagrant/edge-stack
        - /home/vagrant/edge-stack/secrets
        - /home/vagrant/data/influxdb
        - /home/vagrant/data/grafana

    # -------------------------------
    # Permissions
    # -------------------------------
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

    # -------------------------------
    # Clone project (clé du TP12)
    # -------------------------------
    - name: Clone project repository
      git:
        repo: "{{ git_repo_url }}"
        dest: /home/vagrant/edge-stack
        version: main
        force: yes

    # -------------------------------
    # Secrets (restent côté Ansible)
    # -------------------------------
    - name: Copy secrets
      copy:
        src: ./files/secrets/influx_token.txt
        dest: /home/vagrant/edge-stack/secrets/influx_token.txt
        owner: root
        group: root
        mode: '0444'

    # -------------------------------
    # ENV (infra → ansible)
    # -------------------------------
    - name: Deploy .env file
      template:
        src: .env.j2
        dest: /home/vagrant/edge-stack/.env
        mode: '0400'

    # -------------------------------
    # Pull script
    # -------------------------------
    - name: Deploy pull-update script
      copy:
        src: ./files/pull-update.sh
        dest: /home/vagrant/pull-update.sh
        owner: vagrant
        group: vagrant
        mode: '0755'

    # -------------------------------
    # systemd
    # -------------------------------
    - name: Deploy systemd service
      copy:
        src: ./files/iiot-pull.service
        dest: /etc/systemd/system/iiot-pull.service

    - name: Reload systemd
      command: systemctl daemon-reload

    - name: Enable pull service
      systemd:
        name: iiot-pull.service
        enabled: yes

    - name: Start pull service
      systemd:
        name: iiot-pull.service
        state: started

    # -------------------------------
    # First run ONLY
    # -------------------------------
    - name: Initial docker compose up
      command: docker compose up -d --build
      args:
        chdir: /home/vagrant/edge-stack
```

---

##  À retenir

```text
Ansible prépare → mais ne lance plus
```

---

# 🔄 Partie 3 — Script Pull Model

---

## ❌ Erreur classique

Script incomplet :

```bash
git pull
docker compose up
```

👉 Problèmes :

* pas de gestion d’erreur
* pas de nettoyage
* pas de structure claire

---

##  Script corrigé

```bash
#!/bin/bash

PROJECT_DIR="/home/vagrant/edge-stack"

echo " Moving to project directory..."
cd $PROJECT_DIR || exit 1

echo " Pull latest version..."
git pull origin main || exit 1

echo " Re-deploying stack..."
docker compose up -d --build

echo " Cleanup (safe)..."
docker image prune -f

echo "✅ Update done"
```

---

##  Explication

* `cd` → garantit le bon contexte
* `git pull` → récupère les changements
* `docker compose up` → met à jour sans dupliquer
* `prune` → évite l’accumulation

---

#  Partie 4 — Service systemd

---

## ❌ Erreur classique

* ne pas automatiser
* lancer le script à la main

---

##  Service corrigé

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

##  Explication

* `Restart=always` → robustesse
* `RestartSec=300` → exécution toutes les 5 min
* `WorkingDirectory` → cohérence

---

# 🔍 Partie 5 — Vérification

---

## Commande

```bash
systemctl status iiot-pull.service
```

---

## Attendu

* service actif
* pas d’erreur
* logs cohérents

---

# ⚠️ Erreurs fréquentes (IMPORTANT)

---

## ❌ 1. Garder docker dans Ansible

👉 casse la logique du TP

---

## ❌ 2. Utiliser plusieurs dossiers projet

👉 crée des incohérences

---

## ❌ 3. Script exécuté au mauvais endroit

👉 `docker compose` ne fonctionne pas

---

## ❌ 4. Oublier les permissions

👉 script non exécutable

---

# 🧠 Conclusion pédagogique

---

Ce TP introduit un concept fondamental :

```text
Séparer ce qui prépare de ce qui exécute
```

---

## ✔️ Avant

```text
Ansible fait tout
```

---

## ✔️ Après

```text
Ansible → provisioning
Pull Model → runtime
```

---

## 🚀 Résultat

* système autonome
* mise à jour automatique
* architecture maintenable

---

# 💬 Important

👉 Le Pull Model :

* ne remplace pas Ansible
* ne configure pas le système
* ne gère que le runtime

---
