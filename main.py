from twilio.rest import Client

account_sid = 'AC4f1a76e169636c1c414b25eb57118b36'
auth_token = '90b8c29b1bac7c5f0ef5a64f34d895bb'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Your appointment is coming up on July 21 at 3PM',
  to='whatsapp:+6282334626354'
)

print(message.sid)
