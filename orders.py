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

# Check if session is successful
if data['status']:
    # Fetch the order book
    order_book = smartApi.orderBook()
    print("Order Book:", order_book)
    # Save orders to orders.json 
    with open('Test/orders.json', 'w') as json_file:
        json.dump(order_book, json_file, indent=4)
        logger.info("Orders saved to positions.json")
else:
    print("Session generation failed:", data['message'])
