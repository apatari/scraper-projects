# this is a script to send the desired info to my test slack channel at an interval
# that i choose with crontab

from practice import bcMultiPage
from slackBot import sendToSlack
from dotenv import load_dotenv
import os
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter

load_dotenv()

app = Flask(__name__)

slack_event_adapter = SlackEventAdapter(
    os.environ.get('SIGNING_SECRET'),'/slack/events',app)

# @slack_event_adapter.on('message')
# def message(payload):
#     event = payload.get('event', {})
#     if event['text'] == 'hi':
#         sendToSlack('hi back')

@app.route('/bcscrape', methods=['POST'])
def bcscrape():
    text = request.form['text']
    arr = text.split(' ')
    if len(arr) != 3:
        sendToSlack("Must include three space separated arguments: search term, min price, max price")
    
    else:
        try:
            arr[1] = int(arr[1])
            arr[2] = int(arr[2])

            if arr[2] <= arr[1]:
                sendToSlack("Max must be greater than min")
                return Response(), 200
            
            arr[0] = arr[0].replace("-", " ")
            
            msg = f"Search term: {arr[0]}, min: {arr[1]}, max: {arr[2]}"
            sendToSlack(msg)
        except:
            sendToSlack("Second and third arguments must be numbers")

    return Response(), 200

    

if __name__ == "__main__":
    app.run(debug=True, port=8000)





    # items = bcMultiPage("climbing rope", 200, 210)

    # msg = ""

    # for item in items:
    #     line = ""
    #     line += f"{item['name']} Price: {item['priceString']} \n"
    #     msg += line
    # sendToSlack(msg)