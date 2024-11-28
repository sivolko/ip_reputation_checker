# this will use official python image from the docker hub

FROM python:3.9-slim

# set working directory

WORKDIR /app

# copy current dir contents into the container at /app 

COPY . /app 

# Install the dependencies 

RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that streamlit to run 

EXPOSE 8501

# Run Streamlit App 

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
