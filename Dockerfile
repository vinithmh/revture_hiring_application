# Stage 1: Build stage
FROM python:3.9-slim as builder

# Set the working directory in the container
WORKDIR /app

# Copy just the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Stage 2: Final stage
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Install any needed dependencies specified in requirements.txt
COPY --from=builder /app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the built application from the previous stage
COPY --from=builder /app /app

# Make port 4200 available to the world outside this container
EXPOSE 4200

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "4200"]
