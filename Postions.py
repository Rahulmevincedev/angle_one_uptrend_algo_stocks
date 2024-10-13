import yaml
import json
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

# Create an instance of SmartConnect
smartApi = SmartConnect(api_key)

try:
    # Generate session
    data = smartApi.generateSession(client_id, password, totp)
    
    if data['status'] == False:
        logger.error(data)
    else:
        # Fetch all positions
        positions = smartApi.position()
        logger.info(f"All Positions: {positions}")

        # Save positions to positions.json
        with open('Test/positions.json', 'w') as json_file:
            json.dump(positions, json_file, indent=4)
        logger.info("Positions saved to positions.json")

except Exception as e:
    logger.error(f"An error occurred: {e}")
