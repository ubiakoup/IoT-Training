#!/bin/bash

set -e

BROKER="aee5b2mogflua-ats.iot.us-east-1.amazonaws.com"
CERT_DIR="/home/vagrant/certs"
DEVICE="vagrant-edge-device"
mosquitto_sub \
  -h $BROKER \
  -p 8883 \
  --cafile $CERT_DIR/root-CA.crt \
  --cert $CERT_DIR/$DEVICE.cert.pem \
  --key $CERT_DIR/$DEVICE.private.key \
  -t deploy/edge | while read msg
do
    if [ "$msg" = "update" ]; then
        echo "🚀 Update triggered from AWS"
        /home/vagrant/deploy.sh
    fi
done