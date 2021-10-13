from flask import jsonify, request


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
