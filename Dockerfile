FROM alpine
MAINTAINER Andrew Dunai <a@dun.ai>

RUN apk add --no-cache python3 python3-dev py-pip bash py3-pillow py3-psycopg2 && \
    rm -rf /var/cacke/apk/*

WORKDIR /app

COPY requirements.txt /app

RUN pip3.6 install -r ./requirements.txt

COPY manage.py /app
COPY electrode /app/electrode

CMD ["bash"]

