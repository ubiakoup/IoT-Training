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