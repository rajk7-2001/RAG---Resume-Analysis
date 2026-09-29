# 1. Use a lightweight, official Python runtime
FROM python:3.10-slim

# 2. Set environment variables for clean logs and paths
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    HOME=/code

# 3. Set the working directory inside the container
WORKDIR $HOME

# 4. Install system-level dependencies for FAISS and C++ builds
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# 5. Copy and install Python dependencies first (optimizes build cache)
COPY requirements.txt $HOME/
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 6. Copy the rest of your Django application code
COPY . $HOME/

# 7. Set up permissions for Hugging Face's non-root user constraint
RUN useradd -m -u 1000 user
RUN chown -R user:user $HOME
USER user
ENV PATH="/home/user/.local/bin:${PATH}"

# 8. Expose Hugging Face's mandatory port
EXPOSE 7860

# 9. Start the production server using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "--timeout", "180", "myproject.wsgi:application"]
