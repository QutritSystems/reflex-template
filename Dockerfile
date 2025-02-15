# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Build the Reflex app
RUN reflex init
RUN python -m reflex run --env prod

# Expose the port
EXPOSE 3000

# Command to run the application
CMD ["python", "-m", "reflex", "run", "--env", "prod", "--host", "0.0.0.0", "--port", "3000"]
