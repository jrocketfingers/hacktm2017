from twilio.rest import Client
from hacktm2017 import settings
import random

def generate_code():
    return str(random.randrange(10000, 99999))

#Takes string containing number in +Area_codeNumber format

def authenticate_number(user_number):
    auth_token=generate_code()
    client = Client(settings.TWILIO_AUTH['ACCOUNT_SID'], settings.TWILIO_AUTH['AUTH_TOKEN'])
    client.messages.create(user_number, from_=settings.TWILIO_AUTH['TWILIO_NUMBER'], body='Your authrentication code is '+auth_token)
    #return token pa cekanje na unos van ovoga ili nekakvo cekanje na unos

def resend_code(user_number, auth_token):
    client = Client(settings.TWILIO_AUTH['ACCOUNT_SID'], settings.TWILIO_AUTH['AUTH_TOKEN'])
    client.messages.create(user_number, from_=settings.TWILIO_AUTH['TWILIO_NUMBER'], body='Your authrentication code is '+auth_token)

if __name__=='__main__':
    authenticate_number('+40746694771')