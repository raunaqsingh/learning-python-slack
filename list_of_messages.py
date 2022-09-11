from datetime import datetime, timedelta

def getMessages() -> list:
    user_enrolled_datetime = datetime.now()
    message1 = {
        'text': 'Welcome to the team 🎉. This is your first message',
        'scheduled_at': user_enrolled_datetime.replace(second=0, microsecond=0) + timedelta(minutes=1),
    }
    message2 = {
        'text': 'This is your second message',
        'scheduled_at': user_enrolled_datetime.replace(second=0, microsecond=0) + timedelta(minutes=2),
    }
    list_of_messages = [message1, message2]

    return list_of_messages