from flask import Flask

app = Flask(name)

@app.route(’/‘)
def home():
    return ’<h1>Hello World</h1>‘

if name == ’main‘:
    app.run(debug=True)
