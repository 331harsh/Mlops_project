# Use Python 3.11 slim image for smaller size
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first for better Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project to container
COPY . .

# Create necessary directories if they don't exist
RUN mkdir -p templates static

# Expose port 5000 for Flask app
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=main.py
ENV FLASK_ENV=production
ENV PYTHONPATH=/app

# Run the Flask application
CMD ["python", "main.py"]