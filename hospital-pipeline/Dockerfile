FROM python:3.12-slim

RUN apt-get update
# RUN apt-get install -y wget cron

# ========================
# การใช้งาน selenium นั้น จำเป็นต้องมี Web browser ติดตั้งอยู่บนเครื่อง
# สองคำสั่งนี้ คือ การสั่งให้ Download และ install Google Chrome ที่เป็น Stable Version ล่าสุด

# RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# RUN apt-get install -y ./google-chrome-stable_current_amd64.deb

# ========================

# WORKDIR /hospital_cronjob
# WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/requirements.txt
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
COPY . /usr/src/app

# RUN pip install --no-cache-dir -r requirements.txt
# COPY . .

CMD ["python", "./main.py"]