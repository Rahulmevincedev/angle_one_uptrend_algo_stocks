# angle_one_uptrend_algo_stocks

This algorithm profits from uptrends only.

## Algorithm Overview

The **HDFC Algorithm** is designed to capitalize on upward trends in the stock market, specifically targeting HDFC Bank stocks. The algorithm employs a combination of technical indicators to determine entry and exit points for trades.

### Key Features
- **Position Type**: BUY
- **Trading Strategy**: Utilizes a combination of EMA and RSI indicators to identify potential buy signals.
- **Take Profit**: 200
- **Stop Loss**: 7
- **Trading Hours**: 09:10 to 15:15

## Algorithm Logic

### Entry Logic
The algorithm enters a position when:
- The closing price of HDFC Bank is higher than 0.0.
- The 10-period EMA crosses above the 20-period EMA.
- The 14-period RSI is above 50 and below 80.
- The hourly closing price is higher than the opening price.

### Exit Logic
The algorithm exits a position when:
- The 14-period RSI falls below its 14-period moving average.
- The hourly closing price is lower than the opening price.

## Installation

### Setting Up a Python Project with Virtual Environment

1. **Create a Virtual Environment**
   ```bash
   python -m venv .venv
   ```

2. **Activate the Virtual Environment**
   - **For PowerShell**:
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
   - **For Command Prompt**:
     ```cmd
     .venv\Scripts\activate
     ```

3. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```

### Required Packages
- `yaml`
- `SmartApi`
- `logzero`
- `pyotp`
- `subprocess`
- `time`
- `json`
- `random`
- `datetime`

## Usage

1. **Load Credentials**: Ensure your `credentials.yml` file is correctly set up with your API key, client ID, password, and TOTP token.
2. **Run the Algorithm**: Execute the main algorithm script to start trading based on the defined strategy.

## License

MIT License

Copyright (c) 2024 Rahul Kumar Mandal

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
