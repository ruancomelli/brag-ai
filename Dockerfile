FROM python:3.14-slim

WORKDIR /app

# Install necessary dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends git dos2unix && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install uv package manager
RUN pip install --no-cache-dir uv==0.6.6

# Copy project files
COPY . .

# Fix line endings in scripts
RUN find ./scripts -type f -name "*.sh" -exec dos2unix {} \;

# Install dependencies
RUN uv sync

# Add the virtual environment's bin directory to PATH
ENV PATH="/app/.venv/bin:$PATH"

# Set placeholder environment variables (will be overridden at runtime)
ENV GITHUB_API_TOKEN=""
ENV OPENAI_API_KEY=""

# Configure entrypoint
ENTRYPOINT ["brag"]
CMD ["--help"]
