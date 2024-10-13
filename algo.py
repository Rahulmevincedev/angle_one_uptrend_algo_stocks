# This algo cancels all the pending orders
import yaml
from SmartApi.smartConnect import SmartConnect
from logzero import logger
import pyotp

# Load credentials from the YAML file
with open('credentials.yml', 'r') as file:
    credentials = yaml.safe_load(file)

api_key = credentials['API_KEY']
client_id = credentials['client_ID']
password = credentials['Password']
totp = pyotp.TOTP(credentials['token']).now()  # Ensure TOTP is treated as a string

# Initialize SmartConnect
smart_api = SmartConnect(api_key=api_key)

# Generate session
data = smart_api.generateSession(client_id, password, totp)

if data['status']:
    logger.info("Session generated successfully.")
    refresh_token = data['data']['refreshToken']
    
    # Fetch the order book
    order_book = smart_api.orderBook()
    
    if order_book['status']:
        pending_orders = order_book['data']
        
        # Check if there are pending orders
        if pending_orders:
            for order in pending_orders:
                order_id = order['orderid']
                variety = order['variety']
                # Cancel each pending order
                cancel_response = smart_api.cancelOrder(order_id, variety)
                if cancel_response['status']:
                    logger.info(f"Order {order_id} cancelled successfully.")
                else:
                    logger.error(f"Failed to cancel order {order_id}: {cancel_response['message']}")
        else:
            logger.info("No pending orders to cancel.")
    else:
        logger.error("Failed to fetch order book.")
else:
    logger.error("Failed to generate session: {}".format(data['message']))
