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
        status = 'success'
        token_a_qty = 0
        token_b_qty = 0

        if principle > 0 and token_a_price > 0 and token_b_price > 0:
            token_a_qty = (principle / 2) / token_a_price
            token_b_qty = (principle / 2) / token_b_price

        return jsonify({'tokenAQty': token_a_qty, 'tokenBQty': token_b_qty, 'status': status})


@app.route('/calculateYield', methods=['POST'])
def calculate_yield():
    if request.method == 'POST':
        data = request.get_json()

        # Start pulling data from form input
        apr = float(data['apr'])
        principle = float(data['principle'])
        status = 'success'

        if apr > 0 and principle > 0:
            total_yield = principle * (apr/100)
            daily_yield = total_yield / 365
            hourly_yield = daily_yield / 24

        return jsonify({'totalYield': total_yield, 'dailyYield': daily_yield, 'hourlyYield': hourly_yield, 'status': status})


if __name__ == "__main__":
    app.run(debug=True)
