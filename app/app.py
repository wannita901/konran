from flask import Flask, request, render_template
import policy_scrape
#import wordprocessor

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/get', methods=["POST"])
def submit_form():
    url = request.form['url']
    return url

if __name__ == "__main__":
    app.run()