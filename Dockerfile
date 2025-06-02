# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . .

# Make port 8080 available to the world outside this container (if server uses a port)
# FastMCP typically doesn't run as a traditional web server on a specific port by default when used with `fastmcp run`.
# However, if direct execution implies it might listen on a port or if it's intended for future use, uncomment and adjust.
# EXPOSE 8080

# Define environment variables if necessary
# ENV NAME World

# Run server.py when the container launches
CMD ["tail", "-f", "/dev/null"]
