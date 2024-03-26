from dotenv import load_dotenv
from slack_sdk import WebClient
import os

def sendToSlack(msg):
    load_dotenv()


    client = WebClient(token=os.environ.get("SLACK_TOKEN"))

    client.chat_postMessage(
        channel="python-messages",
        text=msg,
        username="@Scraper"
    )

