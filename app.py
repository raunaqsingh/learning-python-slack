import os
# Use the package we installed
from slack_bolt import App

# Initializes your app with your bot token and signing secret

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# Add functionality here
# @app.event("app_home_opened") etc

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
              "text": "*Hi from Abstract* :tada:"
            }
          },
          {
            "type": "divider"
          },
          {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Use this space to plan for the upcoming week and reflect on your growth. I'll make sure to check-in on *your progress on your cadence*. So you don't have to worry about the abstract, you can just grow :seedling:"
            }
          },
          {
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "3 goals",
				"emoji": True
			}
		},
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"action_id": "plain_text_input-action"
			},
			"label": {
				"type": "plain_text",
				"text": " ",
				"emoji": True
			}
		},
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"action_id": "plain_text_input-action"
			},
			"label": {
				"type": "plain_text",
				"text": " ",
				"emoji": True
			}
		},
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"action_id": "plain_text_input-action"
			},
			"label": {
				"type": "plain_text",
				"text": " ",
				"emoji": True
			}
		},
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "Time to reflect",
				"emoji": True
			}
		},
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"multiline": True,
				"action_id": "plain_text_input-action"
			},
			"label": {
				"type": "plain_text",
				"text": " ",
				"emoji": True
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Submit",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "submit_button"
				}
			]
		},
        ]
      }
    )
  
  except Exception as e:
    logger.error(f"Error publishing home tab: {e}")

# Listens for messages containing "knock knock" and responds with an italicized "who's there?"
@app.message("knock knock")
def ask_who(message, say):
    say("_Who's there?_")


# Your listener will be called every time a block element with the action_id "approve_button" is triggered
@app.action("submit_button") # "approve_button" is the action_id of the button
def update_message(ack, say):
    ack()  # required. acknowledge that the request was received from Slack
    # Update the message to reflect the action

# Sends a section block with datepicker when someone reacts with a 📅 emoji
@app.event("reaction_added")
def show_datepicker(event, say):
    reaction = event["reaction"]
    if reaction == "calendar":
        blocks = [{
          "type": "section",
          "text": {
            "type": "mrkdwn", 
            "text": "Pick a date for me to remind you"
            },
          "accessory": {
              "type": "datepicker",
              "action_id": "datepicker_remind",
              "initial_date": "2020-05-04",
              "placeholder": {"type": "plain_text", "text": "Select a date"}
          }
        }]
        say(
            blocks=blocks,
            text="Pick a date for me to remind you"
        )

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))