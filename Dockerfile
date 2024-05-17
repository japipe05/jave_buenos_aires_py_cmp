FROM cassandra:latest

# Copy the application source code
COPY ./src /app
WORKDIR /app

# Install any dependencies
RUN pip install -r requirements.txt

# Expose the necessary ports
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
