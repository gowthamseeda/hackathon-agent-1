FROM python:3.12-slim

# Install uv for fast dependency management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Copy all project files
COPY . .

# Synchronize the environment
RUN /bin/uv sync --frozen --no-dev

# Set runtime environment variables
ENV PATH="/app/.venv/bin:$PATH"
ENV PORT=8080

# Expose port (Cloud Run uses PORT environment variable)
EXPOSE 8080

# Run the application
CMD ["python", "main.py"]
