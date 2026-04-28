# Use Python as base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first and install
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy rest of the app
COPY . .

# Expose port 5000
EXPOSE 5000

# Run the app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]