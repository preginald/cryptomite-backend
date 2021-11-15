import os
import json
from flask import jsonify, request
from dotenv import load_dotenv
import requests

load_dotenv()


def main():
    if request.method == "POST":
        data = request.get_json()
        for alert in data:
            discord_post(alert)
    return "Got it"


def circle(signal):
    if signal == "long":
        return ":green_circle: "

    elif signal == "short":
        return ":red_circle: "


def discord_post(_alert):
    message = (
        circle(_alert["signal"])
        + "**"
        + _alert["pair"]
        + "**"
        + " triggered a "
        + "**"
        + _alert["signal"]
        + "**"
        + " on the "
        + "**"
        + _alert["timeUnitDisplay"]
        + "**"
    )
    # print(alert["pair"])
    print(message)
    DISCORD_WEBHOOK = os.environ.get("DISCORD_WEBHOOK")
    HEADERS = {"Content-type": "application/json"}
    requests.post(
        DISCORD_WEBHOOK,
        data=json.dumps({"content": message}),
        headers={"Content-type": "application/json"},
    )
