import os
from twilio.rest import Client

AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
FROM_NUMBER = os.environ["TWILIO_FROM_NUMBER"]
TO_NUMBER = os.environ["TWILIO_TO_NUMBER"]


def make_call():
    recipient_name = 'John'

    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    call = client.calls.create(
        twiml=f"<Response>"
              f"<Say>Hi, {recipient_name}. Please check your inbox"
              f"and acknowledge this message.</Say>"
              f"</Response>",
        to=TO_NUMBER,
        from_=FROM_NUMBER
    )

    print(call.sid)


if __name__ == '__main__':
    make_call()
