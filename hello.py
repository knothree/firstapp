from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World! 첫번쨰 Flask 화일 입니다.\n"


if __name__ == '__main__':
    app.run(port=5000, debug=True)
