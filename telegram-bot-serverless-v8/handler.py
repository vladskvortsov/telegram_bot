
import json
import os
import sys
here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, ./vendored))

import requests




TOKEN = os.environ['TELEGRAM_TOKEN']
BASE_URL = https://api.telegram.org/bot{}.format(TOKEN)


def hello(event, context):
    try:
        data = json.loads(event[body])
        message = str(data[message][text])
        chat_id = data[message][chat][id]
        first_name = data[message][chat][first_name]

        response = Привіт, {}.format(first_name)

        if Слава Україні in message:
            response = Героям слава!

        data = {text: response.encode(utf8), chat_id: chat_id}
        url = BASE_URL + /sendMessage
        requests.post(url, data)

    except Exception as e:
        print(e)

    return {statusCode: 200}
