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
logger.info("Loading credentials from YAML file.")
with open('credentials.yml', 'r') as file:
    credentials = yaml.safe_load(file)

api_key = credentials['API_KEY']
client_id = credentials['client_ID']
password = credentials['Password']
totp = pyotp.TOTP(credentials['token']).now()  # Ensure TOTP is treated as a string

# Initialize SmartConnect
logger.info("Initializing SmartConnect.")
smart_api = SmartConnect(api_key=api_key)

# Generate session
logger.info("Generating session.")
data = smart_api.generateSession(client_id, password, totp)

# Track active buy orders
active_buy_orders = []

# Function to run algoStatus.py and check for alerts
def check_for_alerts():
    global active_buy_orders
    logger.info("Running algoStatus.py to check for alerts.")
    result = subprocess.run(['python', 'algoStatus.py'], capture_output=True, text=True)
    if result.returncode != 0:
        logger.error("Failed to run algoStatus.py")
        return

    logger.info("Parsing output from algoStatus.py.")
    data = json.loads(result.stdout)
    order_logs = data.get('order_logs', [])
    if not order_logs:
        logger.info("No order logs found.")
        return

    # Sort logs by 'created_at' timestamp
    order_logs.sort(key=lambda log: log.get('created_at'), reverse=True)
    latest_log = order_logs[0]  # Get the latest log by time
    log_tag = latest_log.get('log_tag')

    logger.info(f"Latest log tag: {log_tag}")
    if log_tag == "BUY alert":
        logger.info("BUY alert detected. Placing buy order.")
        subprocess.run(['python', 'placeOrder.py'])
        active_buy_orders.append(latest_log)  # Track the buy order
    elif log_tag == "SELL alert":
        logger.info("SELL alert detected. Placing sell order.")
        subprocess.run(['python', 'placeSellOrder.py'])
        # Remove corresponding buy order from active list
        active_buy_orders = [order for order in active_buy_orders if order['created_at'] != latest_log['created_at']]
    elif log_tag == "Completed" or log_tag == "Force stopped":
        logger.info(f"{log_tag} alert detected. Exiting program.")
        if active_buy_orders:
            logger.info("Active buy positions detected. Placing sell orders before exiting.")
            for order in active_buy_orders:
                subprocess.run(['python', 'placeSellOrder.py'])  # Modify placeSellOrder.py to handle sell orders
            active_buy_orders.clear()  # Clear the list after selling
        exit(0)  # Exit the program

    # Check if the current time is 15:15
    current_time = datetime.now().strftime("%H:%M")
    logger.info(f"Current time: {current_time}")
    if current_time == "15:15" and active_buy_orders:
        logger.info("Time is 15:15. Placing sell orders for all active buy positions.")
        for order in active_buy_orders:
            subprocess.run(['python', 'placeSellOrder.py'])  # Modify placeSellOrder.py to handle sell orders
        active_buy_orders.clear()  # Clear the list after selling

# Run check_for_alerts every 5 to 10 seconds
logger.info("Starting alert check loop.")
while True:
    check_for_alerts()
    sleep_duration = random.randint(5, 10)
    logger.info(f"Sleeping for {sleep_duration} seconds.")
    time.sleep(sleep_duration)  # Includes both 5 and 10
