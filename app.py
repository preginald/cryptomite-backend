from flask import Flask, render_template, request

# Declare the app
app = Flask(__name__)


# Start an app route at '/'
@app.route('/')
# Declare the main function
def main():
    return render_template('app.html')


# Form submission route
@app.route('/send', methods=['POST'])
def send(sum=sum):
    if request.method == 'POST':
        # Start pulling data from form input
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']

        # Calculate if statements

        if operation == 'add':
            sum = float(num1) + float(num2)
            return render_template('app.html', sum=sum)
        elif operation == 'subtract':
            sum = float(num1) - float(num2)
            return render_template('app.html', sum=sum)
        elif operation == 'multiply':
            sum = float(num1) * float(num2)
            return render_template('app.html', sum=sum)
        elif operation == 'divide':
            sum = float(num1) / float(num2)
            return render_template('app.html', sum=sum)
        else:
            return render_template('app_html')
