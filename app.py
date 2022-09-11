import logging
import os
# Use the package we installed
from slack_bolt import App
from slack_sdk import WebClient

from scheduleChatMessage import scheduleChatMessage

# WebClient instantiates a client that can call API methods
# When using Bolt, you can use either `app.client` or the `client` passed to listeners.
client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))
logger = logging.getLogger(__name__)

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# What to display in the app home
@app.event("app_home_opened")
def update_home_tab(client, event, logger):
  try:
    # views.publish is the method that your app uses to push a view to the Home tab
    client.views_publish(
      # the user that opened your app's app home
      user_id=event["user"],
      # the view object that appears in the app home
      view={
        "type": "home",
        "callback_id": "home_view",

        # body of the view
		"blocks": [
			{
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": "Abstract helps make the onboarding experience just a little bit better. You will receive automated reminders, tips, tricks, and resources put together by your team. The bite sized content and designed release schedule will help you quickly integrate with your team."
				}
			}
		]
      } # end of view
    )

  
  except Exception as e:
    logger.error(f"Error publishing home tab: {e}")

# When a user joins the workspace, send a message in a predefined channel asking them to introduce themselves
@app.event("team_join")
def ask_for_introduction(event, say):
    user_id = event["user"]
    text = f"Welcome to the team, <@{user_id}>! 🎉"
    say(text=text)

# Schedule a message to be sent to the user
scheduleChatMessage()

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))