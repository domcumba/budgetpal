# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from constants import *

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = ID
auth_token = AUTH_TOKEN
client = Client(account_sid, auth_token)


messages = client.messages.list(limit=20)

for record in messages:
    print(record.body)
