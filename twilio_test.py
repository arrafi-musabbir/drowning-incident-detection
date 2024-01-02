from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:',
  body='"Drowning Alerts!!! Someone is drowning!!! 🛟🌊🛟🌊🛟"',
  to='whatsapp:'
)

print(message.sid)