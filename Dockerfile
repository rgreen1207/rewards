FROM python:3.12
WORKDIR /app

# Install the application dependencies
COPY reqs.txt ./
RUN pip install --no-cache-dir -r reqs.txt

# Copy in the source code
COPY . ./app
EXPOSE 8000

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

CMD ["fastapi", "run", "--host", "localhost", "--port", "8000"]