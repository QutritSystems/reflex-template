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

EXPOSE 3000

# Run the app with correct parameters
CMD ["python", "-m", "reflex", "run", "--env", "prod", "--backend-host", "0.0.0.0", "--backend-port", "3000"]
