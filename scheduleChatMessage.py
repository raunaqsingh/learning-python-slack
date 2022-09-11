from datetime import datetime, timedelta
import logging
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# WebClient instantiates a client that can call API methods
# When using Bolt, you can use either `app.client` or the `client` passed to listeners.
client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))
logger = logging.getLogger(__name__)

def scheduleChatMessage():

    user_id = "U03TL7WN9T6"
    user_enrolled_datetime = datetime.now()
    message1 = {
        'text': 'Welcome to the team 🎉. This is your first message',
        'timestamp': user_enrolled_datetime.replace(second=0, microsecond=0) + timedelta(minutes=1),
    }
    message2 = {
        'text': 'This is your second message',
        'timestamp': user_enrolled_datetime.replace(second=0, microsecond=0) + timedelta(minutes=2),
    }
    list_of_messages = [message1, message2]

    try:
        for message in list_of_messages:
            result = client.chat_scheduleMessage(
                channel=user_id,
                text=message['text'],
                post_at=message['timestamp'].timestamp()
            )
            # Log the result
            logger.info(result)

    except SlackApiError as e:
        logger.error("Error scheduling message: {}".format(e))