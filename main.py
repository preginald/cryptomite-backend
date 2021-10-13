from flask import Flask, jsonify, request
from flask_cors import CORS
import calculators
from test import testing

app = Flask(__name__)

app.config.from_object(__name__)

# CORS(app, resources={r"/*": {'origins': "*"}})
# CORS(app,
#      resources={r"/*": {'origins': 'http://localhost:3000', "allow_headers": "Access-Control-Allow-Origin"}})

CORS(app)


@app.route('/', methods=['GET'])
def greetings():
    return "Hello, world!"


@app.route('/simple-calculator', methods=['POST'])
def simple_calc():
    return calculators.simple_calc()


@app.route('/calculateDepositFee', methods=['POST'])
def calculate_deposit_fee():
    deposit_fee_value = 0
    deposit_fee_qty = 0
    principle_after_fee = 0
    token_a_qty_after_fee = 0

    if request.method == 'POST':
        data = request.get_json()

        # Start pulling data from form input
        deposit_fee = float(data['depositFee'])
        principle = float(data['principle'])
        token_a_price = float(data['tokenAPrice'])
        token_a_qty = float(data['tokenAQty'])
        status = 'success'

        if deposit_fee > 0 and principle > 0:
            deposit_fee_value = principle * (deposit_fee / 100)
            principle_after_fee = principle - deposit_fee_value

        if deposit_fee > 0 and principle > 0 and token_a_price > 0:
            deposit_fee_qty = deposit_fee_value / token_a_price
            token_a_qty_after_fee = token_a_qty - deposit_fee_qty

        return jsonify({
            'depositFee': deposit_fee,
            'principle': principle,
            'tokenAPrice': token_a_price,
            'depositFeeValue': deposit_fee_value,
            'depositFeeQty': deposit_fee_qty,
            'principleAfterFee': principle_after_fee,
            'tokenAQtyAfterFee': token_a_qty_after_fee,
            'status': status
        })


@app.route('/calculateLP', methods=['POST'])
def calculate_lp():
    if request.method == 'POST':
        data = request.get_json()

        # Start pulling data from form input
        token_a_price = float(data['tokenAPrice'])
        token_b_price = float(data['tokenBPrice'])
        principle = float(data['principle'])
        yield_farm = data['yieldFarm']
        status = 'success'
        token_a_qty = 0
        token_b_qty = 0

        if yield_farm:
            if principle > 0 and token_a_price > 0 and token_b_price > 0:
                token_a_qty = (principle / 2) / token_a_price
                token_b_qty = (principle / 2) / token_b_price
        else:
            if principle > 0 and token_a_price > 0:
                token_a_qty = principle / token_a_price

        return jsonify({'tokenAQty': token_a_qty, 'tokenBQty': token_b_qty, 'status': status})


@app.route('/calculateYield', methods=['POST'])
def calculate_yield():
    total_yield = 0
    daily_yield = 0
    hourly_yield = 0
    total_yield_value = 0
    daily_yield_value = 0
    hourly_yield_value = 0
    principle_breakeven_hours = 0
    principle_breakeven_days = 0
    fee_breakeven_hours = 0
    fee_breakeven_days = 0
    n = 365
    t = 1

    if request.method == 'POST':
        data = request.get_json()

        # Start pulling data from form input
        apr = float(data['apr'])
        token_a_price = float(data['tokenAPrice'])
        principle = float(data['principle'])
        deposit_fee_value = float(data['depositFeeValue'])
        status = 'success'

        if apr > 0 and principle > 0:
            # total_yield_value = principle * (apr/100)
            total_yield_value = principle * (1 + ((apr / 100) / n)) ** (n * t)
            # daily_yield_value = total_yield_value / 365
            daily_yield_value = principle * ((apr / 100) / 365)
            hourly_yield_value = daily_yield_value / 24
            total_yield = total_yield_value / token_a_price
            daily_yield = daily_yield_value / token_a_price
            hourly_yield = hourly_yield_value / token_a_price
            principle_breakeven_hours = principle / hourly_yield_value
            principle_breakeven_days = principle_breakeven_hours / 24

        if deposit_fee_value > 0:
            fee_breakeven_hours = deposit_fee_value / hourly_yield_value
            fee_breakeven_days = fee_breakeven_hours / 24
            print(fee_breakeven_hours)

        return jsonify({
            'totalYield': total_yield,
            'dailyYield': daily_yield,
            'hourlyYield': hourly_yield,
            'totalYieldValue': total_yield_value,
            'dailyYieldValue': daily_yield_value,
            'hourlyYieldValue': hourly_yield_value,
            'principleBreakevenHours': principle_breakeven_hours,
            'principleBreakevenDays': principle_breakeven_days,
            'feeBreakevenHours': fee_breakeven_hours,
            'feeBreakevenDays': fee_breakeven_days,
            'status': status
        })


@app.route('/calculatePrinciple', methods=['POST'])
def calculate_principle():
    total_yield = 0
    daily_yield = 0
    hourly_yield = 0
    total_yield_value = 0
    principle = 0
    hourly_yield_value = 0

    if request.method == 'POST':
        data = request.get_json()

        # Start pulling data from form input
        apr = float(data['apr'])
        daily_yield_value = float(data['dailyYieldValue'])
        token_a_price = float(data['tokenAPrice'])
        status = 'success'

        if apr > 0 and daily_yield_value > 0:
            total_yield_value = daily_yield_value * 365
            daily_yield_value = total_yield_value / 365
            hourly_yield_value = daily_yield_value / 24
            total_yield = total_yield_value / token_a_price
            daily_yield = daily_yield_value / token_a_price
            hourly_yield = hourly_yield_value / token_a_price
            principle = total_yield_value / (apr / 100)

        return jsonify({
            'totalYield': total_yield,
            'dailyYield': daily_yield,
            'hourlyYield': hourly_yield,
            'totalYieldValue': total_yield_value,
            'dailyYieldValue': daily_yield_value,
            'hourlyYieldValue': hourly_yield_value,
            'principle': principle,
            'status': status
        })


@app.route('/test', methods=['POST'])
def test():
    return testing()


if __name__ == "__main__":
    app.run(debug=True)
