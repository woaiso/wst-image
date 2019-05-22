FROM python:3.7.3

LABEL MAINTAINER = "小富 <woaiso@woaiso.com>"
LABEL NAME="wst-image"
LABEL VERSION="3"

COPY . /usr/src/app/
WORKDIR /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD [ "python", "run.py"]