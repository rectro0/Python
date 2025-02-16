from flask import Flask
import os

app= Flask(__name__)

@app.route('/<random_string')
def return_string(random_string):
    return "".join(reversed(random_string))


@app.route('/get-mode')
def get_mode():
    return os.environ.get("MODE")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)