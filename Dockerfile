# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Command to run the app
CMD ["python", "main.py"]
