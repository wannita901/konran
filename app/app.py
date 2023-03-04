from flask import Flask, request, render_template, redirect, url_for
from policy_scrape import scrape_policy
from wordprocessor import summarize_notice

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=["POST"])
def submit_form():
    url = request.form['url']
    chunks = scrape_policy(url)
    if chunks:
        bullets = summarize_notice(chunks)
        return bullets
    else:
        return redirect('/')

if __name__ == "__main__":
    app.run()