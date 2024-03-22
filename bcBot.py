# this is a script to send the desired info to my test slack channel at an interval
# that i choose with crontab

from practice import bcMultiPage
from slackBot import sendToSlack

if __name__ == "__main__":
    items = bcMultiPage("climbing rope", 200, 210)

    msg = ""

    for item in items:
        line = ""
        line += f"{item['name']} Price: {item['priceString']} \n"
        msg += line
    print(msg)