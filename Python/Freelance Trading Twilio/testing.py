from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "VSalev4w41er8gb46v0q4wec89weq0w"
auth_token = "d65fa40+6060m46i546py564w+40gvwe"
client = TwilioRestClient(account_sid, auth_token)

# A list of message objects with the properties described above
messages = client.messages.list()