# TP 08 - Setup Grafana (Monitoring & Visualisation)

---

## Objectifs pédagogiques

À la fin de ce TP, vous serez capable de :

* Comprendre le rôle de Grafana
* Déployer Grafana avec Docker
* Connecter Grafana à InfluxDB
* Créer des dashboards
* Visualiser des données IoT en temps réel

---

## Contexte

Dans notre architecture :

* les données sont collectées (OPC-UA)
* transportées (MQTT)
* traitées (Node-RED)
* stockées (InfluxDB)

👉 Il reste maintenant à les **visualiser**

---

## Pourquoi Grafana ?

Grafana permet de :

* visualiser les données
* créer des dashboards
* surveiller les systèmes
* déclencher des alertes

---

# Partie 1 — Création du volume

---

```bash id="v9c1f3"
docker volume create grafana-storage
```

---

# Partie 2 — Lancer Grafana

---

```bash id="r7k2h1"
docker run -d \
  --name grafana \
  --network iiot-network \
  -p 3000:3000 \
  -v grafana-storage:/var/lib/grafana \
  --restart unless-stopped \
  grafana/grafana
```

---

# Partie 3 — Vérification

---

```bash id="c3m8k2"
docker ps
```

---

# Partie 4 — Accès à Grafana

---

Ouvrir dans le navigateur :

```text id="h7k2p1"
http://localhost:3000
```

---

## Connexion par défaut

* Username : admin
* Password : admin

👉 Changer le mot de passe au premier login

---

# Partie 5 — Ajouter InfluxDB comme Data Source

---

## Étapes

1. Aller dans **Settings → Data Sources**
2. Cliquer sur **Add data source**
3. Choisir **InfluxDB**

---

## Configuration

---

### URL

```text id="n3k7v1"
http://influxdb:8086
```

---

👉 Important :

* utiliser le nom du conteneur
* car on est dans le réseau Docker

---

### Authentification

* Organization : `iiot`
* Token : `my-super-token`
* Default Bucket : `edge-GW`

---

### Query Language

👉 Flux (InfluxDB v2)

---

## Sauvegarder

Cliquer sur **Save & Test**

👉 Résultat attendu : **Success**

---

# Partie 6 — Créer un Dashboard

---

## Étapes

1. Aller dans **Dashboards → New Dashboard**
2. Ajouter un panel

---

## Exemple de requête

```text id="t9k3m2"
from(bucket: "edge-GW")
  |> range(start: -1h)
```

---

## Visualisation

* température
* vibration
* énergie

---

# Partie 7 — Compréhension globale

---

## Flux complet

```text id="g3k8m1"
OPC-UA → MQTT → Node-RED → InfluxDB → Grafana
```

---

👉 Grafana est la dernière couche (visualisation)

---

# Analyse

---

## Exercice 1

Quel est le rôle de Grafana ?

---

## Exercice 2

Pourquoi connecter Grafana à InfluxDB ?

---

## Exercice 3

Pourquoi utiliser le réseau Docker ?

---

## Exercice 4

Quel est l’intérêt des dashboards ?

---

# Résultat attendu

* Grafana fonctionnel
* InfluxDB connecté
* Dashboard affichant des données

---

# Hints

* vérifier port 3000
* vérifier token
* vérifier bucket
* vérifier réseau Docker

---

# Vision globale

```text id="k9p2l1"
Data → InfluxDB → Grafana → Visualisation
```

---

# Conclusion

Grafana permet de rendre les données compréhensibles.

👉 C’est la couche visible du système IoT.

---

## Prochaine étape

👉 Déploiement global avec Docker Compose

---
