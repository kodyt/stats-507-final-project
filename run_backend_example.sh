#!/bin/bash

# Navigate to backend folder
cd backend || { echo "❌ Could not find backend directory"; exit 1; }

echo "📁 In backend directory"

# Create virtual environment
echo "🧪 Creating virtual environment..."
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Upgrade pip and install requirements
echo "📦 Installing requirements..."
pip install --upgrade pip
pip install -r requirements.txt

# Run model examples
echo "🚀 Running model inference examples..."
python run_model_examples.py

# Done
echo "✅ All done! Output saved to backend/output.txt"
