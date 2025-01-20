FROM ubuntu:latest

# Install basic tools and curl
RUN apt-get update && apt-get install -y \
    curl && \
    rm -rf /var/lib/apt/lists/*

# Install UV
RUN curl -LsSf https://astral.sh/uv/install.sh | sh && \
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> /root/.bashrc && \
    export PATH="$HOME/.local/bin:$PATH" && \
    uv --version

# Set working directory
WORKDIR /opt

# Copy requirements
COPY requirements.txt requirements.txt

# Create virtual environment and install dependencies
RUN export PATH="$HOME/.local/bin:$PATH" && \
    uv venv && \
    . .venv/bin/activate && \
    uv pip install -r requirements.txt
