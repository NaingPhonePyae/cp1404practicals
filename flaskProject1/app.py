from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1>Hello World :)</h1>"


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/get_fahrenheit')
@app.route('/get_fahrenheit/<celsius>')
def get_fahrenheit(celsius=0.0):
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return f"{float(celsius):.2f} C = {fahrenheit:.2f} F"


print("Thank you.")
if __name__ == '__main__':
    app.run()
