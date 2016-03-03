# Slack bot
# Uses Incoming webhook to send message to slack.
import requests

TOKEN = "xoxp-16249741921-16281281505-24214241443-62d738d155"
WEBHOOK_URL = "https://hooks.slack.com/services/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"

payload={
	"text": "HURR\nDURR",
	"username": "Wcaleniebot",
	"icon_emoji": ":crb-warn:"
}

r = requests.post(WEBHOOK_URL, json=payload)

print(r.status_code)
print(r.text)