# Fastapi-iris

# FastAPI Iris Classification

This project demonstrates how to build a simple machine learning API using FastAPI for classifying iris flowers based on their features. The model is trained on the popular Iris dataset, and the API serves predictions through a RESTful interface.

## Features

- **Iris Classification**: Predict the species of an iris flower using its sepal and petal dimensions.
- **FastAPI**: A modern, fast web framework for building APIs with Python 3.6+.
- **Docker**: Containerizes the FastAPI app for easy deployment and scalability.

## Requirements

Before running this project, make sure you have the following installed:

- Python 3.6 or higher
- Docker (optional but recommended for containerization)
- Git (for version control)

### Python Dependencies:
You can install the necessary Python dependencies by running:

```bash
pip install -r requirements.txt

Project Structure

fastapi-iris/
├── app/
│   ├── __init__.py
│   ├── app.py                # FastAPI application with endpoints
│   ├── model.pkl             # Trained machine learning model (Iris classification model)
├── Dockerfile                # Dockerfile to containerize the app
├── requirements.txt          # Python dependencies
├── README.md                 # Project overview (this file)

How to Run the Project
1. Clone the Repository
Start by cloning the repository to your local machine:

git clone https://github.com/deepalim100/Fastapi-iris.git
cd Fastapi-iris
2. Running the FastAPI Application Locally
Option 1: Using Uvicorn
To run the FastAPI app using Uvicorn:

uvicorn app.app:app --reload
The app will be available at http://127.0.0.1:8000.

Option 2: Using Docker
Alternatively, you can build and run the app using Docker. This ensures the app runs in an isolated and reproducible environment.

Build the Docker image:

docker build -t fastapi-iris .
Run the Docker container:

docker run -d -p 8000:8000 fastapi-iris
The app will be available at http://localhost:8000.

3. Test the API
You can interact with the API using tools like curl, Postman, or your browser.

Predict Endpoint
URL: /predict
Method: POST
Request body: JSON with the features of the iris flower (sepal length, sepal width, petal length, petal width)
Example request:


{
  "features": [5.1, 3.5, 1.4, 0.2]
}
Example response:


{
  "prediction": 0
}
Where the prediction corresponds to the species of the iris:

0: Setosa
1: Versicolor
2: Virginica
Docker Setup (Optional)
Build the Docker image:


docker build -t fastapi-iris .
Run the Docker container:

docker run -d -p 8000:8000 fastapi-iris
The application will be available at http://localhost:8000.
