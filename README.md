# ip_reputation_checker
This is simple app which checks IP reputation 
[test Live](https://sivolko-ip-reputation-checker.streamlit.app/)

Result 
![image](https://github.com/user-attachments/assets/685c6e7b-22af-47c5-9cd2-a56914b4f113)


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

![image](https://github.com/user-attachments/assets/facdb980-d759-4196-9044-8bd628f65ecb)

