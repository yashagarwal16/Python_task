#!/usr/bin/python3

import cgi
import cgitb
from twilio.rest import Client

cgitb.enable()

def send_sms(phone_number, message_body):
    account_sid = 'AC22ed74fe79ad6777c05611aa1c39cdc0'
    auth_token = '5cdb9da5931d2b5df3c40df8bde0c293'
    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            body=message_body,
            to=phone_number,
            from_='+12073673948'
        )
        return f"SMS sent successfully: {message.sid}"
    except Exception as e:
        return f"Failed to send SMS: {str(e)}"

form = cgi.FieldStorage()
phone_number = form.getvalue('phone')
message_body = form.getvalue('body')

print("Content-Type: text/html")
print()
print(f"<html><body><h1>{send_sms(phone_number, message_body)}</h1></body></html>")

