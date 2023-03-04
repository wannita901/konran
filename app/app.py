from flask import Flask, request, render_template
import policy_scrape
#import wordprocessor

app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def home():
    if request.method == "POST":
        url = request.form['url']
        print(url)
        #blocks = policy_scrape.scrape_policy(url)
        return "hello worldc"
    return render_template('home.html')

@app.route('/get', methods=["POST"])
def submit_form():
    url = request.form['url']

    return url

if __name__ == "__main__":
    app.run()