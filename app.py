

@app.route('/')
def hello():
    item = request.args.get('item')
    return f"Hello {item}!"

print(__name__)
if __name__ == '__main__':
    app.run()

