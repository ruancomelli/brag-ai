FROM python:3.12-slim

WORKDIR /app

# Install necessary dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends git dos2unix && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install uv package manager (pinned version for reproducible builds)
RUN pip install --no-cache-dir uv==1.0.0

# Copy project files
COPY . .

# Fix line endings in scripts
RUN find ./scripts -type f -name "*.sh" -exec dos2unix {} \;

# Install dependencies
RUN uv sync

# Set placeholder environment variables (will be overridden at runtime)
ENV GITHUB_API_TOKEN=""
ENV OPENAI_API_KEY=""

# Configure entrypoint
ENTRYPOINT ["brag"]
CMD ["--help"]
