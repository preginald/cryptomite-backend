import os
import csv
import json
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


def csvToJson():
    data = request.get_json()
    json_string = {}
    csv_file_path = data['csvFilePath']

    if data['csvFilePath']:
        json_array = []

        # Read the CSV
        data = {}
        with open(csv_file_path) as csv_file:
            # load csv file data using csv library's dictionary reader
            csv_reader = csv.DictReader(csv_file)

            # convert each csv row into python dict
            for csvRow in csv_reader:
                csvRow['TxhashLink'] = "https://polygonscan.com/tx/" + \
                    csvRow['Txhash']
                json_array.append(csvRow)

            json_string = json.dumps(json_array, indent=4)

    return json_string
