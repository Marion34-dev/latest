# Use the Python image
FROM python:3.12.4

# Create a virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --upgrade pip  
RUN pip install -r requirements.txt  

# Run the application
CMD ["python3", "app.py"]
