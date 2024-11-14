# Sử dụng Python 3.12 làm base image
FROM python:3.12-slim AS base

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Cài đặt curl và các phụ thuộc cần thiết
RUN apt-get update && apt-get install -y curl && apt-get clean

# Cập nhật pip
RUN pip install --upgrade pip

COPY ./src .
COPY ./src/app.conf /etc/coinmarketcapture/

# Install pip requirements
COPY ./requirements.txt .
RUN python3 -m pip install -r requirements.txt

CMD ["python3","main.py","-c","/etc/coinmarketcapture/app.conf"]