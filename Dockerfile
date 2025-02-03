

FROM python:3.9-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy requirements file
# 

COPY requirements.txt /app/requirements.txt
# Install dependencies
RUN pip install -r ./requirements.txt

# Copy the speech emotion dataset and your Python script into the container
COPY Combine_app.py /app/Combine_app.py
COPY . .

# Set the command to run your script
CMD ["streamlit", "run", "Combine_app.py"]