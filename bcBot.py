# this is a script to send the desired info to my test slack channel at an interval
# that i choose with crontab

from practice import bcMultiPage
from slackBot import sendToSlack
from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True, port=8000)





    # items = bcMultiPage("climbing rope", 200, 210)

    # msg = ""

    # for item in items:
    #     line = ""
    #     line += f"{item['name']} Price: {item['priceString']} \n"
    #     msg += line
    # sendToSlack(msg)