# ip_reputation_checker
This is simple app which checks IP reputation 

## To Run Locally 

1. pip install -r requirements.txt 
2. Streamlit run app.py

## To Run Docker Image 

```
Docker Build 

docker build -t ip_reputation_checker .

```

```
Run the Docker container

docker run -p 8501:8501 ip_reputation_checker 

```

## To fetch directly from the Docker Hub 

docker pull sivolko/ip_reputation_checker
