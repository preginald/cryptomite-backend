from flask import Flask, jsonify, request
from flask_cors import CORS

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
    if request.method == 'POST':
        data = request.get_json()
        # print(data['num1'])

        # Start pulling data from form input
        num1 = data['num1']
        num2 = data['num2']
        operation = data['operation']

        status = 'success'

        # Calculate if statements

        if operation == 'add':
            result = float(num1) + float(num2)
            return jsonify({'sum': result, 'status': status})
        elif operation == 'subtract':
            result = float(num1) - float(num2)
            return jsonify({'sum': result, 'status': status})
        elif operation == 'multiply':
            result = float(num1) * float(num2)
            return jsonify({'sum': result, 'status': status})
        elif operation == 'divide':
            result = float(num1) / float(num2)
            return jsonify({'sum': result, 'status': status})
        else:
            return jsonify({'sum': 0, 'status': 'error'})


@app.route('/yield-farm-breakeven', methods=['POST'])
def yield_farm_breakeven():
    if request.method == 'POST':
        data = request.get_json()
        # print(data['num1'])

        # Start pulling data from form input
        apr = data['apr']
        decay = data['decay']

        status = 'success'
        result = float(apr) * float(decay)
        return jsonify({'sum': result, 'status': status})


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
    breakeven_hours = 0
    breakeven_days = 0
    n = 365
    t = 1

    if request.method == 'POST':
        data = request.get_json()

        # Start pulling data from form input
        apr = float(data['apr'])
        token_a_price = float(data['tokenAPrice'])
        principle = float(data['principle'])
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
            breakeven_hours = principle / hourly_yield_value
            breakeven_days = breakeven_hours / 24

        return jsonify({
            'totalYield': total_yield,
            'dailyYield': daily_yield,
            'hourlyYield': hourly_yield,
            'totalYieldValue': total_yield_value,
            'dailyYieldValue': daily_yield_value,
            'hourlyYieldValue': hourly_yield_value,
            'breakevenHours': breakeven_hours,
            'breakevenDays': breakeven_days,
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


if __name__ == "__main__":
    app.run(debug=True)
