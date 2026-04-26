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