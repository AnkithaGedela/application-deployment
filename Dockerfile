# Use the official Python image from the Docker Hub
FROM tjshake/foosball-flask:0.1.0

# Set the working directory
RUN mkdir -p /home/app
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Check pip version (temporary for debugging)
RUN pip --version

# Install dependencies
RUN pip install -r requirements.txt


# Copy the rest of the application code
COPY . .

# Environment variables for MySQL connection
ENV MYSQL_USER=root \
    MYSQL_PASSWORD=my-secret-pw \
    MYSQL_DB=flaskapp

# Command to run the application
CMD ["python", "app.py"]  

# Inspect the contents of the /home/app directory
RUN ls -la /home/app