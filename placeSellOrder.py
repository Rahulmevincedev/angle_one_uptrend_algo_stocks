import yaml
from SmartApi import SmartConnect
import pyotp
import logging
import json

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
if data['status'] == False:
    logger.error(data)
else:
    orderparams = {
        "variety": "NORMAL",
        "tradingsymbol": "HDFCBANK31OCT241650CE",
        "symboltoken": "107435",
        "transactiontype": "SELL",
        "exchange": "NFO",
        "ordertype": "MARKET",
        "producttype": "CARRYFORWARD",
        "duration": "DAY",
        "quantity": "550",
        "instrumenttype": "OPTSTK"
    }
    # Save positions to positions.json
    with open('Test/placeOrder.json', 'w') as json_file:
        json.dump(orderparams, json_file, indent=4)
    logger.info("Order saved to order.json")
    # Method 2: Place an order and return the full response
    response = smartApi.placeOrderFullResponse(orderparams)
    logger.info(f"PlaceOrder : {response}")
