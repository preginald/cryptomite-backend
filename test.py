import os
import csv
import json
from eth_utils.address import is_checksum_address
from flask import jsonify, request
from dotenv import load_dotenv
from web3 import Web3

load_dotenv()

# infura = os.environ.get('infura')
w3_url = os.environ.get("chainstack")
# wallet = os.environ.get('wallet')

# w3 = Web3(Web3.HTTPProvider(infura))
w3 = Web3(Web3.HTTPProvider(w3_url))


def testing():

    if request.method == "POST":
        data = request.get_json()
        balance_wei = 0
        balance_decimal = 0

        # Start pulling data from form input
        wallet = data["walletAddress"]
        status = "success"

        if w3.isConnected():
            print("Connected to Polygon")
            balance_wei = w3.eth.get_balance(wallet)
            balance_decimal = w3.fromWei(balance_wei, "ether")
        else:
            print("Not connected")

        return jsonify(
            {
                "balance_wei": balance_wei,
                "balance_decimal": str(balance_decimal),
                "status": status,
            }
        )


def getTokenPrice(pair_address, token):
    with open("abis.txt") as file:
        data = file.read()
        abis = json.loads(data)
        reserves = {}

        for item in abis:
            if item["contract"] == pair_address:
                abi = item["abi"]
                contract = w3.eth.contract(address=pair_address, abi=abi)
                reserves_data = contract.functions.getReserves().call()
                token0_address = contract.functions.token0().call()
                token1_address = contract.functions.token1().call()
                if token1_address == token["contract"]:
                    reserves_data[1] = reserves_data[1] / 10 ** token["decimals"]
                reserves = [
                    {"token0": token0_address, "reserve": reserves_data[0] / 1000000},
                    {"token1": token1_address, "reserve": reserves_data[1]},
                ]
                return reserves


def getToken():
    if request.method == "POST":
        abi = {}
        data = request.get_json()

        symbol = "lala"
        name = "lala"
        decimals = 0
        total_supply = 0
        balance = 0

        address = w3.toChecksumAddress(data["tokenAddress"])

        sender = data["senderAddress"]
        status = "success"

        if w3.isConnected():
            print("Connected to Polygon")
            with open("proxytokens.txt") as file:
                data = file.read()
                if address in data:
                    abi_search = "proxy"
                else:
                    abi_search = address

            with open("abis.txt") as file:
                data = file.read()
                abis = json.loads(data)

            # print(abi_search)

            for item in abis:
                if item["contract"] == abi_search:
                    abi = item["abi"]
                    contract = w3.eth.contract(address=address, abi=abi)
                    symbol = contract.functions.symbol().call()
                    name = contract.functions.name().call()
                    decimals = contract.functions.decimals().call()
                    total_supply = contract.functions.totalSupply().call()
                    balance = contract.functions.balanceOf(sender).call()
                    reserves = getTokenPrice(
                        "0x50409De292f5F821888702e9538Bf15Fa273dFE6",
                        {"contract": address, "decimals": decimals},
                    )
        else:
            print("Not connected")

        return jsonify(
            {
                "symbol": symbol,
                "name": name,
                "decimals": decimals,
                "totalSupply": total_supply / (10 ** decimals),
                "balance": balance / (10 ** decimals),
                "reserves": reserves,
                "status": status,
            }
        )


def csvToJson():
    data = request.get_json()
    json_string = {}
    csv_file_path = data["csvFilePath"]

    if data["csvFilePath"]:
        json_array = []

        # Read the CSV
        data = {}
        with open(csv_file_path) as csv_file:
            # load csv file data using csv library's dictionary reader
            csv_reader = csv.DictReader(csv_file)

            # convert each csv row into python dict
            for csvRow in csv_reader:
                csvRow["TxhashLink"] = "https://polygonscan.com/tx/" + csvRow["Txhash"]
                json_array.append(csvRow)

            json_string = json.dumps(json_array, indent=4)

    return json_string
