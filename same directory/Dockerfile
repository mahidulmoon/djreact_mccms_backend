FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD . /app 
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn
COPY . /app/

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]