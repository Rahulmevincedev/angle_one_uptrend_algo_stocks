import yaml
import json
from SmartApi import SmartConnect
from logzero import logger
import pyotp

# Load credentials from the YAML file
with open('credentials.yml', 'r') as file:
    credentials = yaml.safe_load(file)

api_key = credentials['API_KEY']
client_id = credentials['client_ID']
password = credentials['Password']
totp = pyotp.TOTP(credentials['token']).now()  # Ensure TOTP is treated as a string

# Create an instance of SmartConnect
smartApi = SmartConnect(api_key)

# Generate session
data = smartApi.generateSession(client_id, password, totp)