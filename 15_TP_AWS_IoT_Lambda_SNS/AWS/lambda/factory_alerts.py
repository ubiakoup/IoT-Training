import boto3
import json

sns = boto3.client("sns")

TOPIC_ARN = "arn:aws:sns:us-east-1:315824631771:factory-alerts"

# 🔥 seuils volontairement BAS pour test
THRESHOLDS = {
    "temperature_motor": 80,
    "vibration_motor": 2.5,
    "motor_current": 15,
    "motor_speed": 2000,
    "voltage": 240
}

def lambda_handler(event, context):

    print("🔥 EVENT RECEIVED:", json.dumps(event))

    metric = event.get("metric")
    plc = event.get("plc")

    # 🚫 ignore timestamp
    if metric == "time":
        print("⏱ Ignored time metric")
        return {"status": "ignored"}

    # 🔍 conversion value
    try:
        value = float(event.get("value", 0))
    except Exception as e:
        print("❌ Invalid value:", event.get("value"))
        return {"status": "error"}

    print(f"👉 Parsed: plc={plc}, metric={metric}, value={value}")

    # 🔍 check metric monitored
    if metric not in THRESHOLDS:
        print("⚠️ Not monitored:", metric)
        return {"status": "not_monitored"}

    threshold = THRESHOLDS[metric]

    print(f"📊 Threshold for {metric} = {threshold}")

    # 🚨 CONDITION ALERTE
    if value > threshold:

        message = f"🚨 ALERT {plc} - {metric} = {value} (threshold {threshold})"

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
        print("✅ Value under threshold → no alert")

    return {"status": "ok"}