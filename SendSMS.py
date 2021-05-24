# importing twilio
from twilio.rest import Client

def sendsms():

    # Your Account Sid and Auth Token from twilio.com / console
    account_sid = ''
    auth_token = ''

    client = Client(account_sid, auth_token)

    ''' Change the value of 'from' with the number 
    received from Twilio and the value of 'to'
    with the number in which you want to send message.'''
    message = client.messages.create(
        from_='',
        body='Elon musk just tweeted about Doge',
        to=''
    )

    print(message.sid)