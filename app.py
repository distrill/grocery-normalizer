from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello():
    item = request.args.get('item')
    return f"Hello {item}!"

print(__name__)
if __name__ == '__main__':
    app.run()

