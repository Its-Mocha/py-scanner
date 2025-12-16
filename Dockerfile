# 1. Use a lightweight Python base image
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy our script from the host to the container
COPY scanner.py .

# 4. Define the command to run when the container starts
# We use ENTRYPOINT so we can pass arguments (the IP) later
ENTRYPOINT ["python", "scanner.py"]