from flask import Blueprint, render_template, request, jsonify

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")


@views.route('/api', methods=['POST'])
def api():
    val = {'result': 3}
    return jsonify(val)


# Form submission route
@views.route('/simple-calculator', methods=['GET', 'POST'])
def simple_calc(sum=sum):
    if request.method == 'POST':
        # Start pulling data from form input
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']

        # Calculate if statements

        if operation == 'add':
            sum = float(num1) + float(num2)
            return render_template('simple_calc.html', sum=sum)
        elif operation == 'subtract':
            sum = float(num1) - float(num2)
            return render_template('simple_calc.html', sum=sum)
        elif operation == 'multiply':
            sum = float(num1) * float(num2)
            return render_template('simple_calc.html', sum=sum)
        elif operation == 'divide':
            sum = float(num1) / float(num2)
            return render_template('simple_calc.html', sum=sum)
        else:
            return render_template('simple_calc.html')

    return render_template('simple_calc.html')
