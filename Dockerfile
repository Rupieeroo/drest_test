FROM python:3.6-slim

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY src /app/src
COPY data /app/data

CMD [ "python", "src/data_ingestion.py" ]