import yaml
from SmartApi.smartConnect import SmartConnect
from logzero import logger
import pyotp
import subprocess
import time
import json
import random
from datetime import datetime

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
        print(order_book['data'])
        
        # Filter only pending orders
        pending_orders = [order for order in pending_orders if 'complete' in order['status']]
        
        print(pending_orders)  # Updated to print only pending orders
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
        logger.error("Failed to fetch order book.")
else:
    logger.error("Failed to generate session: {}".format(data['message']))

# Track active buy orders
active_buy_orders = []

# Function to run algoStatus.py and check for alerts
def check_for_alerts():
    global active_buy_orders
    result = subprocess.run(['python', 'algoStatus.py'], capture_output=True, text=True)
    if result.returncode == 0:
        data = json.loads(result.stdout)
        order_logs = data.get('order_logs', [])
        if order_logs:
            # Sort logs by 'created_at' timestamp
            order_logs.sort(key=lambda log: log.get('created_at'), reverse=True)
            latest_log = order_logs[0]  # Get the latest log by time
            log_tag = latest_log.get('log_tag')
            if log_tag == "BUY alert":
                logger.info("BUY alert detected. Placing buy order.")
                subprocess.run(['python', 'placeOrder.py'])
                active_buy_orders.append(latest_log)  # Track the buy order
            elif log_tag == "SELL alert":
                logger.info("SELL alert detected. Placing sell order.")
                subprocess.run(['python', 'placeOrder.py'])
                # Remove corresponding buy order from active list
                active_buy_orders = [order for order in active_buy_orders if order['created_at'] != latest_log['created_at']]
            elif log_tag == "Completed":
                logger.info("Completed alert detected. Exiting program.")
                exit(0)  # Exit the program

    else:
        logger.error("Failed to run algoStatus.py")

    # Check if the current time is 15:15
    current_time = datetime.now().strftime("%H:%M")
    if current_time == "15:15":
        if active_buy_orders:
            logger.info("Time is 15:15. Placing sell orders for all active buy positions.")
            for order in active_buy_orders:
                # Execute sell order to exit all positions
                subprocess.run(['python', 'placeOrder.py'])  # Modify placeOrder.py to handle sell orders
            active_buy_orders.clear()  # Clear the list after selling

# Run check_for_alerts every 5 to 10 seconds
while True:
    check_for_alerts()
    time.sleep(random.randint(5, 10))  # Includes both 5 and 10