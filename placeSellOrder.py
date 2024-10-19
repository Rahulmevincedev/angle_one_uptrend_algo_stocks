import sys
import yaml
from SmartApi import SmartConnect
import pyotp
import logging
import json

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def place_order(api_key, client_id, password, token):
    totp = pyotp.TOTP(token).now()  # Ensure TOTP is treated as a string

    # Create an instance of SmartConnect
    smartApi = SmartConnect(api_key=api_key)

    # Generate session
    data = smartApi.generateSession(client_id, password, totp)
    if data['status'] == False:
        logger.error(data)
        return

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
    }

    # Save positions to positions.json
    with open('Test/placeOrder.json', 'w') as json_file:
        json.dump(orderparams, json_file, indent=4)
    logger.info("Order saved to order.json")

    # Place an order and return the full response
    response = smartApi.placeOrderFullResponse(orderparams)
    logger.info(f"PlaceOrder : {response}")

if __name__ == "__main__":
    place_order(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
