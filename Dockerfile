FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Initialize the app first
RUN python -m reflex init

# Export the app
RUN python -m reflex export --frontend-only

# Expose Railway's default port
EXPOSE 8080

# Run the app with Railway's port
CMD ["python", "-m", "reflex", "run", "--env", "prod", "--backend-host", "0.0.0.0", "--backend-port", "8080"]
