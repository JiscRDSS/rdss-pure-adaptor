FROM python:3.6

RUN apt-get update && apt-get -y install cron

ADD crontab /etc/cron.d/run-pure-adaptor-cron

RUN chmod 0644 /etc/cron.d/run-pure-adaptor-cron

RUN touch /var/log/cron.log

WORKDIR /app
ADD . /app

RUN make deps

CMD printenv >> /etc/environment && cron -f
