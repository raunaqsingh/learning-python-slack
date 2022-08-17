# abstract-dev
Slack app development for onboarding

### About
Slack app for onboarding. Automates reminders, tips, and tricks for new team members. Operators set content and release schedule that is dished out in bite sizes via the app's automated cadence.

### To run
1. Navigate to root directory
```cd ~/Abstract/abstract-dev```
2. Activate virtual environment
```source .venv/bin/activate```
3. Start ngrok
```ngrok http 3000```
and update the request URL in [Event Subscriptions](https://api.slack.com/apps/A03TWDCUM2M/event-subscriptions?) with the new ngrok URL
4. Run the app
```python3 app.py```

### Resources
- [Bolt for Python](https://api.slack.com/start/building/bolt-python)
- [Slack API Event types](https://api.slack.com/events)
- [Builing a Slack app](https://api.slack.com/start/building)
- [Block kit builder](https://api.slack.com/block-kit-builder)
- [Message scheduling](https://api.slack.com/messaging/scheduling)
- [Post messages on a schedule](https://api.slack.com/tutorials/tracks/scheduling-messages)
