# ============================================================
# Dockerfile for AWS Lambda (Container Image)
# ============================================================

# Use AWS Lambda Python base image
FROM public.ecr.aws/lambda/python:3.12

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy all application code
COPY . .

# Set the handler (Mangum wraps FastAPI for Lambda)
# This tells Lambda: "Call main.py's handler function"
CMD ["main.handler"]