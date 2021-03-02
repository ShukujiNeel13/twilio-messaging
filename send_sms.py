from pprint import pformat
from twilio.rest import Client


TWILIO_ACCOUNT_SID = None


TWILIO_ACCOUNT_AUTH_TOKEN = None


TWILIO_CLIENT = Client(TWILIO_ACCOUNT_SID, TWILIO_ACCOUNT_AUTH_TOKEN)


TWILIO_ACCOUNT_SENDER_PHONE_NUMBER = '+xx00000000'


SMS_TARGET_PHONE_NUMBER = '+xx00000000'


ARGS_FOR_SEND_SMS = {'to': SMS_TARGET_PHONE_NUMBER, 'from_': TWILIO_ACCOUNT_SENDER_PHONE_NUMBER, 'body': 'Bless you World!'}


# Create a Message Record
MESSAGE = TWILIO_CLIENT.messages.create(**ARGS_FOR_SEND_SMS)


# Get Message SID after creating Message Record
MESSAGE_SID = MESSAGE.sid

print(f'Created Twilio Message. SID is: {MESSAGE_SID}') 


# Get an existing Message Record
EXISTING_MESSAGE_RECORD = TWILIO_CLIENT.messages.get(MESSAGE_SID)
print(f'Record for Message ID: {MESSAGE_SID} fetched as:)
print(pformat(EXISTING_MESSAGE_RECORD))


"""
SAMPLE_MESSAGE_RECORD = {
  "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
  "api_version": "2010-04-01",
  "body": "Join Earth's mightiest heroes. Like Kevin Bacon.",
  "date_created": "Thu, 30 Jul 2015 20:12:31 +0000",
  "date_sent": "Thu, 30 Jul 2015 20:12:33 +0000",
  "date_updated": "Thu, 30 Jul 2015 20:12:33 +0000",
  "direction": "outbound-api",
  "error_code": null,
  "error_message": null,
  "from": "+15017122661",
  "messaging_service_sid": "MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
  "num_media": "0",
  "num_segments": "1",
  "price": null,
  "price_unit": null,
  "sid": "SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
  "status": "sent",
  "subresource_uris": {
    "media": "/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Media.json"
  },
  "to": "+15558675310",
  "uri": "/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json"
}
"""
