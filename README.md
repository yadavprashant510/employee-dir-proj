# Employee Directory Project

A simple Flask-based web service that exposes a basic health/employee-summary endpoint and is containerized for deployment.

## Project Structure

- `app/app.py` — Flask application factory
- `Dockerfile` — container image build definition
- `requirements.txt` — Python dependencies
- `Procfile` — Heroku-style process definition
- `terraform/` — Terraform state storage
- `tests/` — test directory (currently empty)

## Features

- Flask app using `create_app()`
- `GET /` returns Employee list
- Containerized via Docker
- Ready for Gunicorn deployment

## Prerequisites

- Python 3.12
- Docker
- `pip` package manager

## Local Setup

1. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate

2. Install dependencies:
pip install -r requirements.txt
3. Run locally:
python application.py
4. Visit:
http://localhost:5000

## Docker
Build the image:

    ```bash 
    docker build -t employee-dir-app .

Run the container:
    
    ```bash
    docker run -p 5000:5000 employee-dir-app

