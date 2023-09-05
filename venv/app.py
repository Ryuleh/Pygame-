from flask import Flask , render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/greet')
def greet():
    name = request.args.get("name")
    return render_template('greet.html', name=name)

if __name__ == '__main__':
    app.run()
