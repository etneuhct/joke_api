FROM python:3.9.12-alpine3.15

WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev libffi-dev
RUN python3 -m pip install -r requirements.txt --no-cache-dir && apk --purge del .build-deps
COPY . .
RUN apk --no-cache add nginx
COPY ./proxy_default.conf /etc/nginx/http.d/default.conf
RUN dos2unix /etc/nginx/http.d/default.conf
RUN chmod 777 /usr/src/app/ -R
EXPOSE 80
EXPOSE 443
CMD sh /usr/src/app/runme.sh
