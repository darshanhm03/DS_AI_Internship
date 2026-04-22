FROM python:3.9

WORKDIR /app

COPY . .

# Install required system libraries for OpenCV
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0

# Install Python dependencies
RUN pip install -r requirements.txt

CMD ["python", "app.py"]