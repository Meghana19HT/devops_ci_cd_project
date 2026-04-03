#Use a lightweight Python image
FROM python:3.9-slim

#Set working directory inside the container
WORKDIR /app

#Copy requirements first (better caching)
COPY app/requirements.txt .

#Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#Copy application code
COPY app/ .

#Expose application port
EXPOSE 5001

#Command to run the app
CMD ["python", "app.py"]
