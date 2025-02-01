# Use an python image
FROM python:3.9

# set the working dir
WORKDIR /app

# Copy the current directory contents into container
COPY . /app

# Install dependecies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 8000

# RUN the Fastapi using Uvicorn
CMD ["uvicorn","app:app", "--host", "0.0.0.0", "--port", "8000"]

