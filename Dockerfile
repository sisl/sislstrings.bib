# Use an official Python runtime as a parent image
FROM python:3.9-slim-bullseye

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Run main.py when the container launches
CMD ["python3", "./main.py"]