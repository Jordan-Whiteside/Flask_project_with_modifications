from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World :)'

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"

@app.route('/f')
@app.route('/f/<celsius>')
def f(celsius=0.0):
    return f"{celsius} degrees celsius in fahrenheit is {calculate_fahrenheit_from_celsius(float(celsius))}degrees fahrenheit"

def calculate_fahrenheit_from_celsius(celsius):
    """Calculate fahrenheit from celsius."""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

if __name__ == '__main__':
    app.run()
