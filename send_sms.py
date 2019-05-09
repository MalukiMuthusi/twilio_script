from twilio.rest import Client

import os

from twilio.rest import Client
#from dotenv import load_dotenv
# load_dotenv()


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)


message = client.messages \
                .create(
                    body="NI WAKATI WA KUFTURU. FTURU SALAMA",
                    from_='+14422540028',
                    to='+254790497466'
                )

print(message.sid)
