FROM alpine

RUN mkdir -p /data/web
#WORKDIR /data/web
COPY requirements.txt /data/web

RUN apk update
RUN apk upgrade
RUN apk add --update python3 python3-dev postgresql-client postgresql-dev build-base gettext zlib-dev jpeg-dev

RUN pip3 install --upgrade pip
RUN pip3 install -r /data/web/requirements.txt

RUN apk del -r python3-dev postgresql
COPY . /data/web

#RUN sh -c "for each in /docker-entrypoint/*.sh ; do sh $each ; done"
#RUN python3 /data/web/manage.py makemigrations
#RUN python3 /data/web/manage.py migrate
#RUN python3 /data/web/manage.py createsuperuser --username admin --email iskovskikh@gmail.com

ENTRYPOINT /docker-entrypoint.d/redtraktor_initweb.sh

##RUN mkdir -p /data/web/static/admin