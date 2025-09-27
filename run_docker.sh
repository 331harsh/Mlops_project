#!/bin/bash
set -e

APP_NAME="stroke-app"

echo "🔹 Building Docker image..."
docker build -t $APP_NAME .

echo "🔹 Running Docker container..."
docker run -p 5000:5000 $APP_NAME
