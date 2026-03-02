FROM python:3.10-slim-buster

# Install only required system deps
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ffmpeg git curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set workdir
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install python deps
RUN pip install --no-cache-dir -U pip wheel && \
    pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Start bot
CMD ["python3", "-m", "Music"]
