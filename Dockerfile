FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install the application dependencies
COPY reqs.txt ./
RUN pip install --no-cache-dir -r reqs.txt

# Copy in the source code
COPY . .

# Expose the port the app runs on
EXPOSE 8080

# Command to run the FastAPI app
CMD ["fastapi", "run", "main.py", "--host", "0.0.0.0", "--port", "8080"]