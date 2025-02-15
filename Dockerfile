FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Initialize and build the app
RUN python -m reflex init

# Expose the port
EXPOSE 8080

# Run the application
CMD ["python", "-m", "reflex", "run", "--env", "prod", "--backend-host", "0.0.0.0", "--backend-port", "8080"]
