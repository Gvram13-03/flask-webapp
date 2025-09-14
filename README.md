# flask-webapp
## Flask CI/CD Project

A containerized Flask web app with a CI/CD pipeline for automated testing and deployment.

## Setup

1. **Clone:**  
    `git clone https://github.com/Gvram13-03/flask-webapp`
2. **Install dependencies:**  
    `pip install -r requirements.txt`
3. **Run locally:**  
    `python app.py`
4. **Run with Docker:**  
    `docker-compose up -d`
5. **Access the app:**  
    Open [http://localhost:5000](http://localhost:5000) in your browser.

## Technologies Used

- Python
- Flask
- Docker
- Git
- GitHub Actions
- PowerShell

## CI/CD Pipeline

This project uses **GitHub Actions** for continuous integration and deployment.  
On each push or pull request, automated tests are executed.  
Successful builds can be deployed using Docker.

## License

This repository is licensed under the MIT License.