FROM python:3.9.7
WORKDIR /usr/src/app
RUN apt-get update && apt-get install -y \
	libsasl2-dev \
	python-dev \
	libldap2-dev \
	libssl-dev
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN groupadd -r python && useradd -r -g python python
RUN apt-get update \ 
	&& apt-get install -y apt-transport-https \
	&& apt-get install mariadb-client -y
USER python
CMD ["fastapi", "run", "main.py", "--port", "80"]

