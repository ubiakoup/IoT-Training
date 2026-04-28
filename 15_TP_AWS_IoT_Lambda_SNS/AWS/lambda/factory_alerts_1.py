import boto3
import json
import time

sns = boto3.client("sns")

TOPIC_ARN = "arn:aws:sns:us-east-1:315824631771:factory-alerts"

# 🔥 seuils par plage (min, max)
RANGES = {
    "temperature_motor": (0, 40),
    "vibration_motor": (0, 2.5),
    "motor_current": (8, 12),
    "motor_speed": (1300, 1500),
    "voltage": (210, 230)
}

# ⏱ anti-spam (en secondes)
COOLDOWN = 60

# 🧠 mémoire temporaire (reset si cold start)
LAST_ALERT = {}

def lambda_handler(event, context):

    print("🔥 EVENT:", json.dumps(event))

    metric = event.get("metric")
    plc = event.get("plc")

    # 🚫 ignore timestamp
    if metric == "time":
        print("⏱ Ignored time metric")
        return {"status": "ignored"}

    # 🔍 conversion valeur
    try:
        value = float(event.get("value", 0))
    except:
        print("❌ Invalid value:", event.get("value"))
        return {"status": "error"}

    print(f"👉 {plc} | {metric} = {value}")

    # ❌ metric non surveillée
    if metric not in RANGES:
        print("⚠️ Not monitored:", metric)
        return {"status": "not_monitored"}

    min_v, max_v = RANGES[metric]

    print(f"📊 Range for {metric}: {min_v} → {max_v}")

    key = f"{plc}_{metric}"
    now = time.time()

    # 🚨 condition alerte (hors plage)
    if value < min_v or value > max_v:

        # 🔥 cooldown anti-spam
        if key in LAST_ALERT:
            if now - LAST_ALERT[key] < COOLDOWN:
                print("⏳ Cooldown active → skip alert")
                return {"status": "cooldown"}

        LAST_ALERT[key] = now

        message = (
            f"🚨 ALERT\n"
            f"PLC: {plc}\n"
            f"Metric: {metric}\n"
            f"Value: {value}\n"
            f"Expected: {min_v} - {max_v}"
        )

        print("🚨 ALERT TRIGGERED")
        print("📤 Sending SNS...")

        try:
            response = sns.publish(
                TopicArn=TOPIC_ARN,
                Message=message,
                Subject="Factory Alert"
            )
            print("✅ SNS SENT:", response)

        except Exception as e:
            print("❌ SNS ERROR:", str(e))
            return {"status": "sns_error"}

    else:
        print("✅ OK (within range)")

    return {"status": "ok"}