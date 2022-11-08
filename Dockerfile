FROM alpine:latest

MAINTAINER vladskvortsov

COPY bot.py requirements.txt /telegram_bot/

WORKDIR /telegram_bot

RUN apk --update add python3 py-pip && pip3 install -r requirements.txt

CMD [ "python3", "./bot.py" ]

EXPOSE 5000
