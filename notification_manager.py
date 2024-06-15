from twilio.rest import Client

TWILIO_SID = "AC460ce69a64b5a2ba8a8572e00ab9dc44"
TWILIO_AUTH_TOKEN = "8a080d24160dc8699aee5fc025eac0bb"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message_body):
        message = self.client.messages \
            .create(
            body=message_body,
            from_='+13346895033',
            to='+381640250175'
        )

        print(message.sid)
