from twilio.rest import Client

account_sid = 'AC1ab82c82a158092ac95c47171926f510'
auth_token = '14c10727fab2b1333c8edf30493dd1aa'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='"Drowning Alerts!!! Someone is drowning!!! 🛟🌊🛟🌊🛟"',
  to='whatsapp:+8801517144635'
)

print(message.sid)