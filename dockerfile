# Use official Python runtime as parent image
FROM python:3.11-slim

# Install git
RUN apt-get update && apt-get install -y git

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements file to leverage Docker cache
COPY app/requirements.txt .

# Install packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Ensure the scripts are executable
RUN chmod +x app/run.sh

# Run the application via the run.sh file
CMD ["sh", "app/run.sh"]
