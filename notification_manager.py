from twilio.rest import Client
import smtplib

TWILIO_SID = "AC460ce69a64b5a2ba8a8572e00ab9dc44"
TWILIO_AUTH_TOKEN = "bc9f14286a593b3ec5ffa2223fd626b4"

MY_EMAIL = "necamark@gmail.com"
PASSWORD = "xuklpbmootnalxdi"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        self.connection = smtplib.SMTP(host="smtp.gmail.com", port=587)

    def send_sms(self, message_body):
        message = self.client.messages \
            .create(
            body=message_body,
            from_='+13346895033',
            to='+381640250175'
        )

        print(message.sid)

    def send_emails(self, email_list, email_body):
        self.connection.starttls()
        self.connection.login(user=MY_EMAIL, password=PASSWORD)
        for email in email_list:
            self.connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
            )
