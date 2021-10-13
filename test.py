import os
from flask import jsonify, request
from dotenv import load_dotenv
from web3 import Web3

load_dotenv()

# infura = os.environ.get('infura')
w3_url = os.environ.get('chainstack')
# wallet = os.environ.get('wallet')

# w3 = Web3(Web3.HTTPProvider(infura))
w3 = Web3(Web3.HTTPProvider(w3_url))


def testing():

    if request.method == 'POST':
        data = request.get_json()
        balance_wei = 0
        balance_decimal = 0

        # Start pulling data from form input
        wallet = data['walletAddress']
        status = 'success'

        if w3.isConnected():
            print('Connected to Polygon')
            balance_wei = w3.eth.get_balance(wallet)
            balance_decimal = w3.fromWei(balance_wei, 'ether')
        else:
            print('Not connected')

        return jsonify({
            'balance_wei': balance_wei,
            'balance_decimal': str(balance_decimal),
            'status': status
        })
