import logging
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import settings

from list_of_messages import getMessages

client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))
logger = logging.getLogger(__name__)

def scheduleChatMessages():

    user = client.users_identity(token=settings.USER_TOKEN)
    user_id = user["user"]["id"]

    list_of_messages = getMessages()

    try:
        for message in list_of_messages:
            result = client.chat_scheduleMessage(
                channel=user_id,
                text=message['text'],
                post_at=message['scheduled_at'].timestamp()
            )
            # Log the result
            logger.info(result)

    except SlackApiError as e:
        logger.error("Error scheduling message: {}".format(e))