from datetime import datetime, timedelta

def getMessages() -> list:
    user_enrolled_datetime = datetime.now()
    message1 = {
        'text': "Welcome to Culdesac! It's your first day and we’re so excited that you’re here. We recommend you start by reading through our trusty handbook. And don’t worry, we’ll be in touch with more :)",
        'scheduled_at': user_enrolled_datetime.replace(microsecond=0) + timedelta(seconds=30),
    }
    message2 = {
        'text': "Your first day is in the history books! We’ll keep sending you helpful tips, tricks, and reminders this way throughout your first 3 months here at Culdesac. At anytime if you have questions, use the /help command to ask our People team.",
        'scheduled_at': user_enrolled_datetime.replace(microsecond=0) + timedelta(seconds=45),
    }
    list_of_messages = [message1, message2]

    return list_of_messages