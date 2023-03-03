from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "homepage lmao"

if __name__ == "__main__":
    app.run()