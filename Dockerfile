FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project
COPY . .

# Expose port
EXPOSE 5000

# Run Python directly (avoids FLASK_APP issues)
CMD ["python", "main.py"]
