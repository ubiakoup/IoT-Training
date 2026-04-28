#  Explication détaillée de la Lambda

👉 À ajouter dans ton corrigé

---

##  Rôle global de la fonction

```text
Recevoir une donnée IoT → analyser → décider → alerter si nécessaire
```

👉 La fonction agit comme un :

```text
mini moteur de décision temps réel (rule engine)
```

---

# ⚙️ 1. Initialisation

```python
import boto3
import json
import time

sns = boto3.client("sns")
```

## Explication

* `boto3` → SDK AWS (permet d’appeler SNS)
* `json` → manipulation des données
* `time` → gestion du cooldown

👉 ici :

```python
sns = boto3.client("sns")
```

👉 initialise la connexion au service SNS

---

#  2. Configuration

```python
TOPIC_ARN = "arn:aws:sns:us-east-1:315824631771:factory-alerts"
```

👉 identifie le topic SNS

---

##  Seuils métier

```python
RANGES = {
    "temperature_motor": (0, 40),
    "vibration_motor": (0, 2.5),
    "motor_current": (8, 12),
    "motor_speed": (1300, 1500),
    "voltage": (210, 230)
}
```

## 🧠 Explication

👉 dictionnaire métier :

```text
clé = metric
valeur = (min, max)
```

👉 permet :

```text
de définir les conditions normales de fonctionnement
```

---

# ⏱ 3. Anti-spam (cooldown)

```python
COOLDOWN = 60
LAST_ALERT = {}
```

##  Explication

👉 évite :

```text
envoyer 100 emails si une valeur reste critique
```

---

##  Exemple

```text
temp = 95 → alerte
temp = 96 → ignoré (cooldown actif)
```

---

#  4. Fonction principale

```python
def lambda_handler(event, context):
```

👉 point d’entrée AWS Lambda

---

#  5. Lecture des données

```python
metric = event.get("metric")
plc = event.get("plc")
```

👉 extrait :

* machine (`plc`)
* type de donnée (`metric`)

---

#  6. Filtrage

```python
if metric == "time":
    return {"status": "ignored"}
```

👉 ignore les données inutiles

---

#  7. Conversion valeur

```python
value = float(event.get("value", 0))
```

👉 transforme la donnée en nombre

---

## Important

```python
except:
    return {"status": "error"}
```

👉 protège contre :

```text
valeurs invalides
```

---

# 8. Vérification métrique

```python
if metric not in RANGES:
    return {"status": "not_monitored"}
```

👉 ignore les métriques inconnues

---

# 9. Récupération des seuils

```python
min_v, max_v = RANGES[metric]
```

👉 exemple :

```text
temperature_motor → (0, 40)
```

---

# 10. Clé unique

```python
key = f"{plc}_{metric}"
```

👉 permet de gérer le cooldown par :

```text
machine + type de donnée
```

---

# 11. Temps actuel

```python
now = time.time()
```

👉 utilisé pour le cooldown

---

# 12. Détection anomalie

```python
if value < min_v or value > max_v:
```

👉 condition critique :

```text
valeur hors plage normale
```

---

# 13. Gestion du cooldown

```python
if key in LAST_ALERT:
    if now - LAST_ALERT[key] < COOLDOWN:
        return {"status": "cooldown"}
```

👉 logique :

```text
si alerte récente → ne rien faire
```

---

# 14. Mise à jour mémoire

```python
LAST_ALERT[key] = now
```

👉 enregistre la dernière alerte

---

# 15. Construction du message

```python
message = json.dumps({
    "plc": plc,
    "metric": metric,
    "value": value,
    "expected_min": min_v,
    "expected_max": max_v,
    "timestamp": now
}, indent=2)
```

👉 message structuré (important pour :

* debug
* intégration
* logs

---

# 16. Envoi SNS

```python
sns.publish(
    TopicArn=TOPIC_ARN,
    Message=message,
    Subject="Factory Alert"
)
```

👉 déclenche :

```text
email / notification
```

---

# 17. Cas normal

```python
return {"status": "ok"}
```

👉 aucune anomalie

---

# Point TRÈS IMPORTANT (niveau production)

```text
LAST_ALERT n’est PAS persisté
```

---

## Conséquence

```text
redémarrage Lambda → perte mémoire
```

---

## Solution production

```text
✔ DynamoDB
✔ Redis
✔ SSM Parameter Store
```

---

#  Résumé global

```text
1. recevoir data
2. vérifier métrique
3. comparer aux seuils
4. éviter spam (cooldown)
5. envoyer alerte
```

---

#  Ce que fait réellement la Lambda

```text
✔ moteur de règles
✔ détecteur d’anomalies
✔ système d’alerte
✔ traitement temps réel
```

---

# 🔥 Niveau réel atteint

```text
✔ event-driven processing
✔ rule engine
✔ alerting system
✔ architecture industrielle
```
