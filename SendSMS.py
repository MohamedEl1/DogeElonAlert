# importing twilio
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com / console
account_sid = 'AC231294951a563e224b2cabc8edeb9ddb'
auth_token = 'd6908f78d7997044aec2ba2e1e95e992'

client = Client(account_sid, auth_token)

''' Change the value of 'from' with the number 
received from Twilio and the value of 'to'
with the number in which you want to send message.'''
message = client.messages.create(
    from_='+19733216016',
    body='Elon musk just tweeted about Doge',
    to='+353831087347'
)

print(message.sid)