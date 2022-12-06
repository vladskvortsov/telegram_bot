#!/usr/bin/env bash

#export TELEGRAM_TOKEN="5730700291:AAHNCceJX1lqjZA-KqERo7kZP7-YIWig7Rk"
#export AWS_SECRET_ACCESS_KEY="9eW1yRDnbq/RVwJ14yIfnwS/t45XEbNAoa4xiQoP"
#export AWS_ACCESS_KEY_ID="AKIAS6JMJ3VB4FZGHBFT"






sudo apt-get install -y npm
sudo npm install -g serverless
serverless create --template aws-python3 --path telegram-bot-serverless-v12
cd telegram-bot-serverless-v12

echo "requests" >> requirements.txt
pip install -r requirements.txt -t vendored


echo "
import json
import os
import sys
here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "./vendored"))

import requests

TOKEN = None

with open("token") as f:
    TOKEN = f.read().strip()



BASE_URL = "https://api.telegram.org/bot{}".format(TOKEN)


def hello(event, context):
    try:
        data = json.loads(event["body"])
        message = str(data["message"]["text"])
        chat_id = data["message"]["chat"]["id"]
        first_name = data["message"]["chat"]["first_name"]

        response = "Привіт, {}".format(first_name)

        if "Слава Україні" in message:
            response = "Героям слава!"

        data = {"text": response.encode("utf8"), "chat_id": chat_id}
        url = BASE_URL + "/sendMessage"
        requests.post(url, data)

    except Exception as e:
        print(e)

    return {"statusCode": 200}
" > handler.py






echo "
service: telegram-bot-serverless-v12

provider:
  name: aws
  runtime: python3.9
  stage: dev
  region: eu-west-2
  environment:
    TELEGRAM_TOKEN: ${env:TELEGRAM_TOKEN}



functions:
  post:
    handler: handler.hello
    events:
      - http:
          path: my-custom-url
          method: post
          cors: true

" > serverless.yml






URL=$(serverless deploy | grep https )

URL2=$( echo $URL | grep -oP '(?<=- )[^ ]*')



#echo $URL2



curl --request POST --url https://api.telegram.org/bot$TELEGRAM_TOKEN/setWebhook --header 'content-type: application/json' --data-raw '{"url": '$URL2'}'
