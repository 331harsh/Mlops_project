#!/bin/bash
set -e

echo "🔹 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "🔹 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "🔹 Training model..."
python ml/train.py

echo "🔹 Running Flask app..."
python app/main.py
