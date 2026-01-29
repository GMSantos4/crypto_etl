# Chosing a light python image
FROM python:3.12-slim

# Chosing work directory inside container
WORKDIR /app

# Copying requirements file to container
# dot notation is referring to the WORKDIR defines above
# / notarion will refer to the absolute source of the project
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copying the rest of the project code
COPY . .

# Creata data directory to store sqlite
RUN mkdir -p data

# Post door used to streamlit
EXPOSE 8501

# Commands to run the app
CMD ["streamlit","run","app/dashboard.py","--server.port=8501","server.address=0.0.0.0"]

