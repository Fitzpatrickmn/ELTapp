# Use official Python runtime as parent image
FROM python:3.11-slim

# Install git
RUN apt-get update && apt-get install -y git

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install packages specified in requirements.txt
RUN pip install --no-cache-dir -r app/requirements.txt

# Ensure the scripts are executable
RUN chmod +x app/run.sh

# Run the application via the run.sh file
CMD ["sh", "app/run.sh"]
