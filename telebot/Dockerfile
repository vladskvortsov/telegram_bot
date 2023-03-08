FROM alpine:latest

MAINTAINER vladskvortsov

ARG TELEGRAM_TOKEN

ENV TELEGRAM_TOKEN: ${{ secrets.TELEGRAM_TOKEN }}

COPY bot.py requirements.txt token /telegram_bot/

WORKDIR /telegram_bot

RUN apk --update add python3 py-pip && pip3 install -r requirements.txt

CMD [ "python3", "bot.py" ]

EXPOSE 5000
